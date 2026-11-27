#!/usr/bin/env python3
"""Phase 5 Article bridge: draws_from is owned; informs is query-only."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMON = ROOT / "scripts" / "cme_common.py"
BRIDGE = ROOT / "scripts" / "cme_bridge.py"
SAMPLE = ROOT / "sample-knowledge"
ART = "article.loop-policy.01J8X00000000000000000000B"
FIND = "finding.loop-policy.01J8X000000000000000000005"
AUTHOR = "grok-bot/content-media"


def run_validate(bundle: Path):
    return subprocess.run(
        [sys.executable, str(COMMON), "validate", "--bundle", str(bundle)],
        capture_output=True,
        text=True,
    )


def run_bridge(*args, env=None):
    e = os.environ.copy()
    if env:
        e.update(env)
    return subprocess.run(
        [sys.executable, str(BRIDGE), *args],
        capture_output=True,
        text=True,
        env=e,
    )


def test_sample_validates_with_draws_from():
    r = run_validate(SAMPLE)
    assert r.returncode == 0, r.stdout + r.stderr
    text = (SAMPLE / "articles" / "loop-policy-article.md").read_text()
    assert "draws_from" in text
    assert FIND in text
    assert "rel: informs" not in text


def test_informs_is_fail_closed():
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "k"
        shutil.copytree(SAMPLE, dest)
        p = dest / "articles" / "loop-policy-article.md"
        p.write_text(p.read_text().replace("rel: draws_from", "rel: informs"))
        r = run_validate(dest)
        assert r.returncode != 0, r.stdout
        data = json.loads(r.stdout)
        assert any("informs" in e for e in data["errors"]), data


def test_draws_from_requires_finding_id():
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "k"
        shutil.copytree(SAMPLE, dest)
        p = dest / "articles" / "loop-policy-article.md"
        p.write_text(p.read_text().replace(FIND, "claim.loop-policy.01J8X000000000000000000006"))
        r = run_validate(dest)
        assert r.returncode != 0, r.stdout
        data = json.loads(r.stdout)
        assert any("Finding id" in e for e in data["errors"]), data


def test_idempotent_bridge():
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "k"
        shutil.copytree(SAMPLE, dest)
        p = dest / "articles" / "loop-policy-article.md"
        p.write_text(
            p.read_text().replace(
                f"  - target: {FIND}\n    rel: draws_from\n",
                "",
            )
        )
        a = run_bridge("--bundle", str(dest), "--article", ART, "--finding", FIND, "--author", AUTHOR)
        assert a.returncode == 0, a.stdout + a.stderr
        first = json.loads(a.stdout)
        assert first["wrote"] is True
        assert first["idempotent"] is False
        b = run_bridge("--bundle", str(dest), "--article", ART, "--finding", FIND, "--author", AUTHOR)
        assert b.returncode == 0, b.stdout + b.stderr
        second = json.loads(b.stdout)
        assert second["idempotent"] is True
        assert second["wrote"] is False
        r = run_validate(dest)
        assert r.returncode == 0, r.stdout + r.stderr


def test_bridge_refuses_non_finding():
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "k"
        shutil.copytree(SAMPLE, dest)
        r = run_bridge(
            "--bundle",
            str(dest),
            "--article",
            ART,
            "--finding",
            "claim.loop-policy.01J8X000000000000000000006",
            "--author",
            AUTHOR,
        )
        assert r.returncode != 0
        assert "Finding id" in (r.stdout + r.stderr)


def test_bridge_refuses_existing_informs():
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "k"
        shutil.copytree(SAMPLE, dest)
        p = dest / "articles" / "loop-policy-article.md"
        p.write_text(
            p.read_text().replace(
                "  - target:",
                "  - target: x\n    rel: informs\n  - target:",
            )
        )
        r = run_bridge("--bundle", str(dest), "--article", ART, "--finding", FIND, "--author", AUTHOR)
        assert r.returncode != 0
        assert "informs" in (r.stdout + r.stderr).lower()


if __name__ == "__main__":
    test_sample_validates_with_draws_from()
    test_informs_is_fail_closed()
    test_draws_from_requires_finding_id()
    test_idempotent_bridge()
    test_bridge_refuses_non_finding()
    test_bridge_refuses_existing_informs()
    print("ok")
