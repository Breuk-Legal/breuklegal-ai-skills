# Breuk Legal AI Skills ⚖️ 🤖

> **A curated collection of open-source AI skills, tools, and integrations built for modern LegalTech.**

Welcome to the `breuklegal-ai-skills` repository. This project is maintained by [Breuk Legal](https://breuklegal.com) to provide robust, secure, and ready-to-use AI capabilities for corporate law automation, starting with Colombian law.

## 🧑‍⚖️ For lawyers using ChatGPT, Gemini, or other chat tools

You don't need any technical setup to use the content of these skills.

**ChatGPT (Custom GPTs):** create a Custom GPT, upload the skill's `SKILL.md` and `references` file as knowledge files (up to 20 files allowed), and paste the body of `SKILL.md` as the GPT's instructions.

**Gemini (Gems):** create a Gem, attach the `SKILL.md` and `references` file as knowledge files (up to 10 files, 100MB each — available even on the free plan), and paste the instructions the same way.

Find each skill's files inside its folder, for example: [`colombia-derecho-societario-analisis-constitucion/skills/colombia-derecho-societario-constitucion/`](./colombia/derecho-societario/colombia-derecho-societario-analisis-constitucion/skills/colombia-derecho-societario-constitucion/) or [`colombia-cobro-cartera-gestion-integral/skills/`](./colombia/cobro-cartera/colombia-cobro-cartera-gestion-integral/skills/).

## 🤖 For coding agents (Codex, Antigravity, Cursor, Kiro, Gemini CLI)

Each plugin ships its own `AGENTS.md` (the open standard that 30+ tools read automatically). Just point your agent at the plugin folder you want to use, e.g. [`colombia-derecho-societario-analisis-constitucion/AGENTS.md`](./colombia/derecho-societario/colombia-derecho-societario-analisis-constitucion/AGENTS.md).

You can also install with the [skills.sh](https://www.skills.sh/) CLI — pick the scope you need:

```
# Everything in the repo (both plugins, all skills)
npx skills add Breuk-Legal/breuklegal-ai-skills --all

# A whole plugin (all of its skills) — point at the plugin folder
npx skills add Breuk-Legal/breuklegal-ai-skills/colombia/cobro-cartera/colombia-cobro-cartera-gestion-integral

# A single skill, by its full name (searched across the repo)
npx skills add Breuk-Legal/breuklegal-ai-skills --skill colombia-cobro-cartera-politica

# Preview what's available without installing
npx skills add Breuk-Legal/breuklegal-ai-skills --list
```

Skill names are fully qualified (`{jurisdiction}-{legal-area}-{function}`, e.g. `colombia-cobro-cartera-politica`) because `npx skills add` installs each skill flat into your agent's skills directory with no plugin namespace — see each plugin's README for its skill list.

## 💻 For Claude users (Cowork / Claude Code)

```
/plugin marketplace add Breuk-Legal/breuklegal-ai-skills
/plugin install colombia-derecho-societario-analisis-constitucion@breuklegal-ai-skills
/reload-plugins
```

Claude Code is also supported by the skills.sh CLI, so the same `npx skills add …` commands shown above (all / per-plugin / per-skill) work here too.

## 🎯 What's inside?

This repository contains modular AI tools designed to be easily injected into your LLM orchestration frameworks, agents, and pipelines. Our focus is on bridging the gap between raw legal data and actionable AI logic.

Here you will find:
*   **Legal Data Parsers:** Tools for extracting structured data from contracts and legal documents.
*   **Workflow Integrations:** Connectors for CRMs, e-signature platforms, and document management systems.
*   **Orchestration Nodes:** Skills optimized for AI agent environments and Model Context Protocol (MCP) servers.

### Available skills

| Skill | Description |
|---|---|
| [`colombia-derecho-societario-analisis-constitucion`](./colombia/derecho-societario/colombia-derecho-societario-analisis-constitucion/) | Analyzes and recommends the right corporate vehicle in Colombian law (SAS, S.A., Ltda., branch of a foreign company), including foreign investment. |
| [`colombia-cobro-cartera-gestion-integral`](./colombia/cobro-cartera/colombia-cobro-cartera-gestion-integral/) | Accounts-receivable collection workflow for lawyers/firms managing cartera on behalf of business clients in Colombia — policy setup, invoice classification, drafting, and automated sending with a fixed human-review gate before pre-legal/judicial action. |

## 🛡️ Security & DevSecOps

Handling legal data requires the highest standards of security. All skills in this repository are built with a privacy-first mindset, ensuring that sensitive information is handled securely within your cloud infrastructure. No skill published here contains client data.

## 🤝 Contributing

We believe in building the future of law in public. Pull requests, issue reports, and feature requests are highly welcome. Let's compile a better legal system together.

---
**License:** [MIT License](LICENSE)
