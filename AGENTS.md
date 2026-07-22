# AGENTS.md — breuklegal-ai-skills

This repository groups open-source skills from Breuk Legal for Colombian legal practice, installable in Claude, and compatible with coding agents via AGENTS.md (Codex, Antigravity, Cursor, Kiro, Gemini CLI) and with `npx skills add` (skills.sh).

## Available skills

- **breuk-derecho-societario-colombia** — analyzes and recommends the right corporate vehicle (SAS, S.A., Ltda., branch of a foreign company), including foreign investment. See `breuk-derecho-societario-colombia/AGENTS.md` for details.
- **breuk-cobro-cartera** — accounts-receivable collection workflow for lawyers/firms managing cartera on behalf of business clients in Colombia (4-stage model, policy setup, classification, drafting, automated sending with a fixed human-review gate before pre-legal/judicial). See `breuk-cobro-cartera/AGENTS.md` for details.

## Naming convention

Everything published in this repository (plugins, skills) starts with the `breuk-` prefix.

## Contributing

Before adding a new skill: no client data, normative content verified against a primary source, and its own `AGENTS.md` inside the plugin folder.
