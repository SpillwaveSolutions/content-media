# ADR 002 — Article bridge

Status: accepted. 2026-08-23.

Canonical stored edge: **Article → draws_from → Finding**.

content-media registers and writes this edge. RKC never writes an edge whose target type it does not own. `research-graph` may expose `informs` as a query-only inverse.

## Rules

- Persist only Article → draws_from → Finding.
- Do not persist `informs`.
- Do not mint a second Article type in RKC.
- Do not auto-write `draws_from`.
- Finding target shape: `finding.<subject-slug>.<ulid>`.
- Northstar / Lumenfield samples are fiction only.

## Write path

```
python3 scripts/cme_bridge.py \
  --bundle knowledge \
  --article <article-id-or-slug> \
  --finding finding.<slug>.<ulid> \
  --author grok-bot/content-media
```

See also RKC `docs/adr/002-article-bridge.md`.
