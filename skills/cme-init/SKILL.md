---
name: cme-init
description: Scaffold the Content Media catalogs in a shared second-brain bundle.
---

# cme-init

Create the catalogs this plugin owns inside a shared knowledge root.

## Process

1. Confirm target (default `knowledge/`).
2. Run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/cme_common.py" init-bundle \
  --bundle knowledge \
  --title "Content Media" \
  --catalogs "articles,drafts,series,subscribers,segments,campaigns,experiments"
```

3. Point the user at `sample-knowledge/` for a fictional demo.

## Done when

- `knowledge/index.md` exists
- Each owned catalog has `index.md`
