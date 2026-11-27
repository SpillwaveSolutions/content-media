---
name: cme-validate
description: Validate Content Media concepts: required fields, types, in-bundle links, and the Article → Finding bridge.
---

# cme-validate

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/cme_common.py" validate --bundle knowledge
```

Fail on:

- missing `type` / `title`
- broken absolute in-bundle links
- persisted `informs` (query-only inverse — never store it)
- `draws_from` whose target is not a Finding id (`finding.<slug>.<ulid>`)
