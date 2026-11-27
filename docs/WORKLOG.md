# WikiTicket SDD

This repository uses **WikiTicket SDD** (`worklog`) for visible WIP.

Plugin: https://github.com/SpillwaveSolutions/wiki_ticket_sdd  
Release: v0.24.4

## Install

Claude Code / Grok Build:

```
/plugin marketplace add SpillwaveSolutions/wiki_ticket_sdd
/plugin install worklog
```

Codex: `codex plugin marketplace add SpillwaveSolutions/wiki_ticket_sdd`

Cursor: install via Agent Plugins / `.cursor-plugin` from that repo.

## CLI

```
python3 path/to/wiki_ticket_sdd/bin/worklog add --level story --kind feature "title"
python3 path/to/wiki_ticket_sdd/bin/worklog list
python3 path/to/wiki_ticket_sdd/bin/worklog roadmap-render
```

Do not hand-edit `.work/*.jsonl`.

## 2026-08-23 — Phase 5 Article bridge (0.4.0)

Landed on GitHub without replacing the 20-type ContentPack:

- Register `draws_from` (Article → Finding). content-media owns the write.
- Fail-closed validate on persisted `informs`.
- `/cme-bridge` + `scripts/cme_bridge.py` (idempotent, Finding-id target only).
- Fiction sample `loop-policy-article.md` → `finding.loop-policy.01J8X000000000000000000005`.

RKC must not write this edge. `research-graph` derives `informs` as query-only.
