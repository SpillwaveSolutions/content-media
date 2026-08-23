#!/usr/bin/env python3
"""Write Article → draws_from → Finding. Idempotent. Never writes informs.

content-media owns this edge (RKC ADR 002). RKC never writes it.
research-graph may derive informs as a query-only inverse.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cme_common import (  # noqa: E402
    iter_concepts,
    resolve_author,
    resolve_bundle,
    valid_finding_id,
    write_concept,
)


def find_article(bundle: Path, article: str):
    needle = article.strip()
    for c in iter_concepts(bundle):
        if c["meta"].get("type") != "Article":
            continue
        stem = Path(c["path"]).stem
        if (
            c["meta"].get("id") == needle
            or stem == needle
            or c["path"] == needle
            or c["path"].endswith("/" + needle)
            or c["path"].endswith("/" + needle + ".md")
            or (c["meta"].get("title") or "").lower() == needle.lower()
        ):
            return c
    return None


def add_draws_from(
    bundle: Path,
    article: str,
    finding_id: str,
    *,
    author: str | None = None,
    dry_run: bool = False,
) -> dict:
    if not valid_finding_id(finding_id):
        raise SystemExit(f"draws_from target must be a Finding id, got {finding_id}")
    c = find_article(bundle, article)
    if c is None:
        raise SystemExit(f"unknown article {article}")
    links = [l for l in (c["meta"].get("links") or []) if isinstance(l, dict)]
    for link in links:
        if link.get("rel") == "informs":
            raise SystemExit("refuse to persist informs; it is a query-only inverse")
        if link.get("rel") == "draws_from" and link.get("target") == finding_id:
            return {
                "wrote": False,
                "idempotent": True,
                "article": c["meta"].get("id") or c["path"],
                "finding": finding_id,
                "path": c["path"],
            }
    links.append({"target": finding_id, "rel": "draws_from"})
    meta = dict(c["meta"])
    meta["links"] = links
    if author:
        meta["author"] = author
    if not dry_run:
        write_concept(c["file"], meta, c["body"])
    return {
        "wrote": not dry_run,
        "idempotent": False,
        "article": meta.get("id") or c["path"],
        "finding": finding_id,
        "path": c["path"],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article", required=True, help="Article id, slug, path, or title")
    ap.add_argument("--finding", required=True, help="Finding id (finding.<slug>.<ulid>)")
    ap.add_argument("--bundle", default="")
    ap.add_argument("--author", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    author = resolve_author(args.author or None)
    bundle = resolve_bundle(args.bundle)
    result = add_draws_from(
        bundle, args.article, args.finding, author=author, dry_run=args.dry_run
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
