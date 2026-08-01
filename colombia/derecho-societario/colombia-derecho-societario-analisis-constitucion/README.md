# colombia-derecho-societario-analisis-constitucion

A skill package for analyzing and recommending the right corporate vehicle in Colombian law. It runs in any AI agent environment — Claude Cowork/Code, coding agents that read `AGENTS.md` (Codex, Antigravity, Cursor, Kiro, Gemini CLI), and `npx skills add` (skills.sh). It is not tied to a single platform.

## What's inside

**Skill:** `analisis-constitucion-societaria-colombia`

Helps diagnose the case, compare corporate vehicles (SAS, S.A., Ltda., branch of a foreign company), apply the foreign investment regime when it applies, and structure a full advisory session — with explicit reminders to verify any normative citation against a primary source before a binding document.

## How to use it

If you don't use Claude, see the repository's main README for instructions for ChatGPT, Gemini, and coding agents.

If you use Claude Cowork or Claude Code:

```
/plugin marketplace add Breuk-Legal/breuklegal-ai-skills
/plugin install colombia-derecho-societario-analisis-constitucion@breuklegal-ai-skills
/reload-plugins
```

Or with the skills.sh CLI:

```
npx skills add Breuk-Legal/breuklegal-ai-skills
```

## Scope and limitations

Content validated against primary normative sources in July 2026 (Ley 1258/2008, Ley 2069/2020, Ley 2294/2023, Decreto 1068/2015). Colombian corporate law changes — check the current validity of any cited article before using it in a binding document. This skill does not replace professional legal advice.

## License

MIT — see the repository's [LICENSE](../LICENSE).
