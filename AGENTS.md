# AGENTS.md — breuklegal-ai-skills

This repository groups open-source skills from Breuk Legal for Colombian legal practice, installable in Claude, and compatible with coding agents via AGENTS.md (Codex, Antigravity, Cursor, Kiro, Gemini CLI) and with `npx skills add` (skills.sh).

## Available skills

- **colombia-derecho-societario-analisis-constitucion** — analyzes and recommends the right corporate vehicle (SAS, S.A., Ltda., branch of a foreign company), including foreign investment. See `colombia/derecho-societario/colombia-derecho-societario-analisis-constitucion/AGENTS.md` for details.
- **colombia-cobro-cartera-gestion-integral** — accounts-receivable collection workflow for lawyers/firms managing cartera on behalf of business clients in Colombia (4-stage model, policy setup, classification, drafting, automated sending with a fixed human-review gate before pre-legal/judicial). See `colombia/cobro-cartera/colombia-cobro-cartera-gestion-integral/AGENTS.md` for details.

## Naming convention

Plugins are named `{jurisdiction}-{legal-area}-{skill-type}` (e.g. `colombia-cobro-cartera-gestion-integral`) and live under `colombia/{legal-area}/`. Names are platform- and vendor-neutral: no product or brand prefix.

Skills follow the same rule one level down, `{jurisdiction}-{legal-area}-{function}` (e.g. `colombia-cobro-cartera-politica`), and the directory name must match the `name:` in the skill's frontmatter. The prefix is not redundant: installers such as `npx skills add` drop every skill flat into the agent's skills directory (`.claude/skills/<name>/`), with no plugin namespace, so a generic name like `cobro-setup` would collide with any other publisher's. Renaming a published skill is expensive — it loses its skills.sh entry and its install history — so treat the name as a permanent public identifier.

## Contributing

Before adding a new skill: no client data, normative content verified against a primary source, and its own `AGENTS.md` inside the plugin folder.
