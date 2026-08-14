---
name: cme-validate
description: Validate Content Media concepts: required fields, types, and in-bundle links.
---

# cme-validate

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/cme_common.py" validate --bundle knowledge
```

Fail on missing `type`/`title` or broken absolute links.
