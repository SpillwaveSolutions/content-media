# Changelog

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
