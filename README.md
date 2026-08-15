# Content Media

Content and audience ContentPack: articles, drafts, series, editorial calendar, subscribers, segments, and performance metrics.

MIT. Dual-host: **Claude Code**, **Grok Build**, and **Codex** (Agent Skill Standard). Writes OKF Markdown + YAML into a shared second-brain bundle so other agents and local jobs can read the same graph.

## Install

```bash
# Claude Code
/plugin marketplace add SpillwaveSolutions/content-media
/plugin install content-media@SpillwaveSolutions

# Skilz CLI
skilz install SpillwaveSolutions/content-media
```

Point the plugin at a shared knowledge root (default `knowledge/`). All sibling ContentPack plugins write into the same tree.

## Skills

| Skill | What it does |
|-------|----------------|
| `/cme-init` | Scaffold the catalogs this plugin owns |
| `/cme-capture` | Capture a noun into the shared second brain (deterministic write) |
| `/cme-pack` | Build a bounded ContextPack from a root concept |
| `/cme-validate` | Validate frontmatter, types, and links |
| `/cme-session` | Open or close an isolated write session (worktree + PR) |
| `/cme-doctor` | Health check of the bundle this plugin owns |

## Nouns this plugin may write

| Type | Meaning |
|------|---------|
| `Article` | Published or publishable piece |
| `Draft` | Work in progress |
| `Series` | Named sequence of articles |
| `EditorialCalendar` | Planned publish dates |
| `Headline` | Title variant |
| `Hook` | Opening hook |
| `Outline` | Structure of a piece |
| `KeyPoint` | Claim the piece must land |
| `CallToAction` | What the reader should do |
| `Subscriber` | Audience member or segment proxy |
| `Segment` | Audience cohort |
| `AudienceInsight` | What the audience cares about |
| `PerformanceMetric` | Views, reads, restacks, etc. |
| `DistributionChannel` | Medium, Substack, LinkedIn, etc. |
| `PromotionPlan` | How a piece will be pushed |
| `RepurposingNote` | How to slice the piece |
| `StyleGuide` | Voice and format rules |
| `PositioningStatement` | How we talk about the offer |
| `ContentExperiment` | A/B or format test |
| `Feedback` | Reader or editor feedback |

## Relationships

| `rel` | Meaning |
|-------|---------|
| `authored_by` | Writer identity |
| `belongs_to` | Article in a series |
| `promotes` | Article promotes an offer or idea |
| `engaged_with` | Subscriber engaged with article |
| `distributed_on` | Channel |
| `measured_by` | Has performance metrics |
| `originates_from` | Came from experiment or outline |
| `related_to` | Related pieces |
| `supersedes` | Updated version |

## Catalogs

- `articles/`
- `drafts/`
- `series/`
- `subscribers/`
- `segments/`
- `campaigns/`
- `experiments/`

## Deterministic write boundary

The model proposes. Schema-enforced scripts commit:

```bash
python3 scripts/cme_common.py write \
  --bundle knowledge \
  --type Article \
  --folder articles \
  --title "Example" \
  --author "Grok Bot: Content Media"
```

Never invent `rel` values. Never write types owned by another plugin.



## Related plugins

### ContentPack suite

- [second-brain-core](https://github.com/SpillwaveSolutions/second-brain-core)
- [executive-coordination](https://github.com/SpillwaveSolutions/executive-coordination)
- [account-management](https://github.com/SpillwaveSolutions/account-management)
- [sales-pipeline](https://github.com/SpillwaveSolutions/sales-pipeline)
- [executive-job-search](https://github.com/SpillwaveSolutions/executive-job-search)
- [consulting-leads](https://github.com/SpillwaveSolutions/consulting-leads)
- [content-media](https://github.com/SpillwaveSolutions/content-media)
- [news-digest](https://github.com/SpillwaveSolutions/news-digest)
- [gtm-positioning](https://github.com/SpillwaveSolutions/gtm-positioning)
- [second-brain-marketplace](https://github.com/SpillwaveSolutions/second-brain-marketplace)
- [second-brain-starter](https://github.com/SpillwaveSolutions/second-brain-starter)

### Foundation

- [okf-plugin](https://github.com/SpillwaveSolutions/okf-plugin) — Open Knowledge Format graph engine
- [project-knowledge-capture](https://github.com/SpillwaveSolutions/project-knowledge-capture) — Project Knowledge Capture. The why second brain.
- [system-architecture-capture](https://github.com/SpillwaveSolutions/system-architecture-capture) — System Architecture Capture. The what-is-running second brain.
- [data-engineering-knowledge-capture](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture) — Data Engineering Knowledge Capture. The data-plane second brain.
- [wiki_ticket_sdd](https://github.com/SpillwaveSolutions/wiki_ticket_sdd) — WikiTicket SDD. Visible work log. Append-only ULID JSONL plus fold.
- [okf-agent-graph](https://github.com/SpillwaveSolutions/okf-agent-graph) — AGER. Orchestrator / Doer / Judge / Synthesizer.


## Onboarding

Grok Bot and other host agents should start at [docs/ONBOARDING.md](docs/ONBOARDING.md). That file is the history of the LLM-wiki effort, the destination state (Grok Bots and local agents sharing one git-native second brain), and the canonical public repo list.

## Multi-host

Works with Claude Code, Grok Build, Codex, Agent Plugins 1.0 clients, Grok Bot, and LangChain Deep Agents.

| Host | How to load |
|------|-------------|
| Claude Code | marketplace + plugin install |
| Grok Build | zero-config Claude plugin |
| Codex | Agent Skills / `hooks/hooks.json` |
| Agent Plugins clients | root `plugin.json` + `skills/` |
| Grok Bot | [docs/GROK_BOT.md](docs/GROK_BOT.md) |
| LangChain Deep Agents | [docs/LANG_CHAIN_DEEP_AGENTS.md](docs/LANG_CHAIN_DEEP_AGENTS.md) |

Write isolation (worktree + PR) lives in second-brain-core: [docs/ISOLATION.md](https://github.com/SpillwaveSolutions/second-brain-core/blob/main/docs/ISOLATION.md). Point `SECOND_BRAIN_ROOT` at the session bundle. Never hard-code a private remote.

Eight job-function plugins plus core. Knowledge root is always a local path or env the human already owns.

## License

MIT. Copyright 2026 Rick Hightower / contributors.
