# Breuk Legal AI Skills ⚖️ 🤖

> **A curated collection of open-source AI skills, tools, and integrations built for modern LegalTech.**

Welcome to the `breuklegal-ai-skills` repository. This project is maintained by [Breuk Legal](https://breuklegal.com) to provide robust, secure, and ready-to-use AI capabilities for corporate law automation, con foco inicial en derecho colombiano.

## 🧑‍⚖️ Para abogados que usan ChatGPT, Gemini u otras herramientas de chat

No necesitas instalar nada técnico para aprovechar el contenido de estas skills.

**ChatGPT (Custom GPTs):** crea un Custom GPT, sube el `SKILL.md` y el archivo de `references` de la skill que te interese como archivos de conocimiento (hasta 20 archivos permitidos), y pega el cuerpo del `SKILL.md` como instrucciones del GPT.

**Gemini (Gems):** crea un Gem, adjunta el `SKILL.md` y el archivo de `references` como archivos de conocimiento (hasta 10 archivos, 100MB cada uno — disponible incluso en el plan gratuito), y pega las instrucciones igual que en ChatGPT.

Encuentra los archivos de cada skill dentro de su carpeta, por ejemplo: [`breuk-derecho-societario-colombia/skills/analisis-constitucion-societaria-colombia/`](./breuk-derecho-societario-colombia/skills/analisis-constitucion-societaria-colombia/).

## 🤖 Para agentes de código (Codex, Antigravity, Cursor, Kiro, Gemini CLI)

Cada plugin trae su propio `AGENTS.md` (estándar abierto que más de 30 herramientas leen automáticamente). Solo apunta tu agente a la carpeta del plugin que quieras usar, por ejemplo [`breuk-derecho-societario-colombia/AGENTS.md`](./breuk-derecho-societario-colombia/AGENTS.md).

También puedes instalar cualquier skill con el CLI de [skills.sh](https://www.skills.sh/):

```
npx skills add Breuk-Legal/breuklegal-ai-skills
```

## 💻 Para usuarios de Claude (Cowork / Claude Code)

```
/plugin marketplace add Breuk-Legal/breuklegal-ai-skills
/plugin install breuk-derecho-societario-colombia@breuklegal-ai-skills
/reload-plugins
```

## 🎯 What's inside?

This repository contains modular AI tools designed to be easily injected into your LLM orchestration frameworks, agents, and pipelines. Our focus is on bridging the gap between raw legal data and actionable AI logic.

Here you will find:
*   **Legal Data Parsers:** Tools for extracting structured data from contracts and legal documents.
*   **Workflow Integrations:** Connectors for CRMs, e-signature platforms, and document management systems.
*   **Orchestration Nodes:** Skills optimized for AI agent environments and Model Context Protocol (MCP) servers.

### Skills disponibles

| Skill | Descripción |
|---|---|
| [`breuk-derecho-societario-colombia`](./breuk-derecho-societario-colombia/) | Análisis y recomendación de figura societaria en Colombia (SAS, S.A., Ltda., sucursal), incluyendo inversión extranjera. |

## 📛 Convención de nombres

Todo lo publicado en este repositorio (plugins y skills) empieza con el prefijo `breuk-`.

## 🛡️ Security & DevSecOps

Handling legal data requires the highest standards of security. All skills in this repository are built with a privacy-first mindset, ensuring that sensitive information is handled securely within your cloud infrastructure. Ninguna skill publicada aquí contiene datos de clientes.

## 🤝 Contributing

We believe in building the future of law in public. Pull requests, issue reports, and feature requests are highly welcome. Let's compile a better legal system together.

---
**License:** [MIT License](LICENSE)
