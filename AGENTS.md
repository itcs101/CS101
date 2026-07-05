# AGENTS.md

## Purpose
This repository is primarily a documentation and knowledge base rather than a runnable application.
It contains markdown notes, business modelling artifacts, ontology documents, diagram source files, and some example scripts.

## What agents should know
- Primary work is authoring and editing documentation in Markdown.
- Key folders:
  - `AI/` — AI tools, knowledge graph and LLM notes
  - `business-analysis/` — business analysis and process docs
  - `business-modelling/` — BPMN, ontology, data modelling materials
  - `projects/` — project-specific notes and artifacts
  - `writedocs/` — writing samples and documentation examples
  - `scripts/` — utility scripts, including Python examples
- The repository is not structured as a standard software app. Do not assume there is a web server, package manager setup, or build pipeline unless explicitly present.

## Editing conventions
- Prefer GitHub-flavored Markdown and maintain readability.
- Preserve existing Chinese/English text and formatting unless the user explicitly asks for translation or localization.
- When converting documents, use `pandoc` with `--wrap=none --atx-headers --extract-media=.` to avoid unnecessary reflow and preserve media.
- Diagram source files like `.drawio` should be edited with the VS Code draw.io plugin and exported as SVG where needed for embedding.
- Keep changes local to the existing content structure; do not invent new application layers.

## Notes for AI tools
- If asked to implement code, first verify whether the requested code belongs in `scripts/python/` or is part of an existing project folder.
- If asked to run or suggest commands, confirm the command is supported by the current repo contents before using it.
- Avoid creating a conventional app scaffold or package.json unless the user explicitly requests a new project and there is no existing app structure.

## Useful references
- Root README: `README.md` (documentation editing guidance)
- Example script path: `positional_encoding_example.py`
- Doc conversion example: `writedocs/samples/product01/README.md`
