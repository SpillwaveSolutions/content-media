# Changelog

## 0.4.0 — 2026-08-23

Phase 5 Article bridge (RKC ADR 002). Adds to the existing 20-type ContentPack; does not replace it.

- Register `draws_from` (Article → Finding). content-media owns the write.
- `informs` is a query-only inverse derived by `research-graph`. Never persist. Validate fail-closes on it.
- `scripts/cme_bridge.py` writes the edge idempotently. Finding-id target only.
- Skill `/cme-bridge` + command `commands/cme-bridge.md`.
- Fiction sample `articles/loop-policy-article.md` draws from `finding.loop-policy.01J8X000000000000000000005`.
- Docs: `docs/typed-edges.md`, `docs/adr/002-article-bridge.md`.

## 0.3.4

- WikiTicket SDD (worklog) is the tracking system for this plugin.


## 0.3.3

- Three-host hooks: Codex + Cursor-native when Claude hooks exist.


## 0.3.2 — 2026-08-17

- **Cursor host.** `.cursor-plugin/plugin.json` (Cursor Plugins) plus `.cursor/rules/second-brain.mdc`. Docs: `docs/CURSOR.md`. `docs/GROK_BOT.md` now covers Grok Bot spawning Cursor cloud agents.

## 0.3.1 — 2026-08-16

- Privacy: isolation tests use only fictional **lumenfield-detector** / **northstar-console** actors.


## 0.3.0 — 2026-08-15

- Grok Bot onboarding: `docs/ONBOARDING.md` (LLM-wiki history, destination state, public repo list)
- Full type ownership in `docs/GROK_BOT.md` (every registry noun, not a subset)
- Registry folders filled so writes land in the right catalog
- Linked Northstar sample graph (typed edges, packable in 2 hops)
- Version stamps aligned across plugin.json, marketplace, and package.json
- README related-plugins list now covers the whole suite plus foundations

## 0.2.0 — 2026-08-15

- Write isolation: `scripts/brain_session.py` (worktree + branch + PR)
- Required `--author` / `SECOND_BRAIN_IDENTITY`; emit `WriteEvent` on write
- Session overlay on pack (`--overlay`)
- Agent Plugins 1.0 root `plugin.json`
- `docs/GROK_BOT.md`, `docs/LANG_CHAIN_DEEP_AGENTS.md`, `docs/ISOLATION.md`
- Codex hooks (`.codex-plugin` + `hooks/hooks.json`)
- Host skills for Grok Bot and LangChain Deep Agents

## 0.1.0 — 2026-08-14

- Initial public release
- Nouns: Article, Draft, Series, EditorialCalendar, Headline, Hook, Outline, KeyPoint, CallToAction, Subscriber, Segment, AudienceInsight, PerformanceMetric, DistributionChannel, PromotionPlan, RepurposingNote, StyleGuide, PositioningStatement, ContentExperiment, Feedback
- Skills: cme-init, cme-capture, cme-pack, cme-validate, cme-doctor
- Dual-host plugin manifests (Claude Code + Grok Build)
