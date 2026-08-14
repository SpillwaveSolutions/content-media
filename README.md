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

- [second-brain-core](https://github.com/SpillwaveSolutions/second-brain-core) — shared pack engine and typed-edge conventions
- [project-knowledge-capture](https://github.com/SpillwaveSolutions/project-knowledge-capture) — the “why” second brain
- [system-architecture-capture](https://github.com/SpillwaveSolutions/system-architecture-capture) — the “what is running” second brain
- [wiki_ticket_sdd](https://github.com/SpillwaveSolutions/wiki_ticket_sdd) — visible work log

## License

MIT. Copyright 2026 Rick Hightower / contributors.
