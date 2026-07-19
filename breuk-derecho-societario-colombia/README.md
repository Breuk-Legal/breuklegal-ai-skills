# breuk-derecho-societario-colombia

Claude Cowork / Claude Code plugin with a skill for analyzing and recommending the right corporate vehicle in Colombian law. Also compatible with coding agents that read `AGENTS.md` (Codex, Antigravity, Cursor, Kiro, Gemini CLI) and with `npx skills add` (skills.sh).

## What's inside

**Skill:** `analisis-constitucion-societaria-colombia`

Helps diagnose the case, compare corporate vehicles (SAS, S.A., Ltda., branch of a foreign company), apply the foreign investment regime when it applies, and structure a full advisory session — with explicit reminders to verify any normative citation against a primary source before a binding document.

## How to use it

If you don't use Claude, see the repository's main README for instructions for ChatGPT, Gemini, and coding agents.

If you use Claude Cowork or Claude Code:

```
/plugin marketplace add Breuk-Legal/breuklegal-ai-skills
/plugin install breuk-derecho-societario-colombia@breuklegal-ai-skills
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
