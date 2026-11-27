---
name: cme-bridge
description: Write Article → draws_from → Finding. content-media owns this edge. Never persist informs.
---

# cme-bridge

Canonical stored edge (RKC ADR 002): **Article → draws_from → Finding**.

content-media owns the write. RKC never writes an edge whose target type it does not own. `research-graph` may expose `informs` as a **query-only** inverse. Never persist both directions.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/cme_bridge.py" \
  --bundle knowledge \
  --article <article-id-or-slug> \
  --finding finding.<subject-slug>.<ulid> \
  --author grok-bot/content-media
```

Rules:

- Persist only Article → draws_from → Finding.
- Finding id shape: `finding.<slug>.<26-char-ulid>`.
- Do not persist `informs`.
- Do not write RKC nouns (Claim, Evidence, Finding, …).
- Do not mint a second Article type in RKC.
- Do not auto-write `draws_from` — the human (or this skill, when asked) owns the link.
- Idempotent: adding the same `draws_from` twice is a no-op.
- Fail closed on persisted `informs` or a `draws_from` target that is not a Finding id.

After the write, run `/cme-validate`.
