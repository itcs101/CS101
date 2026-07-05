# Copilot Instructions

## Purpose
This repository is a documentation and knowledge base rather than a standard software application.
AI coding agents should treat it primarily as a markdown authoring and content editing workspace.

## What to focus on
- Keep existing Chinese/English content intact unless the user explicitly asks for translation.
- Prefer lightweight edits and preserve document structure.
- Use `pandoc` for document conversions when requested, especially for `.docx` -> `.md` workflows.
- Use the VS Code draw.io extension for `.drawio` files and export diagrams as SVG when needed for embedding.

## Project conventions
- `AI/` contains AI tool notes, knowledge graph research, and LLM documentation.
- `business-analysis/` contains business analysis and process documents.
- `business-modelling/` contains BPMN, ontology, and data modelling artifacts.
- `projects/` contains project-specific notes.
- `writedocs/` contains writing samples and documentation examples.
- `scripts/` contains utility scripts and examples, including Python.

## Agent behavior
- Do not assume there is a build system, package manager, or runnable app unless the repository explicitly contains one.
- If asked to implement code, verify whether it belongs in `scripts/python/` or an existing project folder.
- If asked to add new functionality, prefer small, localized changes that fit the repository's documentation-first nature.

## Useful references
- Root README: `README.md`
- Example conversion workflow: `README.md` and `writedocs/samples/product01/README.md`
