# HSBC APAC Regulatory Reporting — Consulting Report (English)

Comprehensive consulting report on HSBC Group's Asia-Pacific regulatory reporting system optimization. Targeted at APAC COOs, CDOs/CIOs, and market-level management, covering a panoramic analysis of regulatory reporting requirements across 22 APAC markets.

## Quick Start

```bash
./build_all.sh
```

Generates `HSBC-AME-RR-Summary-en.pdf`.

## Prerequisites

| Tool | Install (macOS) |
|------|-----------------|
| pandoc >= 3.0 | `brew install pandoc` |
| XeLaTeX (MacTeX) | `brew install mactex-no-gui` |
| CJK Fonts | `brew install --cask font-noto-sans-cjk-sc` |
| Python 3 + matplotlib | `pip3 install matplotlib numpy` |
| mermaid-cli | `npm install -g @mermaid-js/mermaid-cli` |

## Directory Structure

```
en/
├── README.md                          # This file
├── build_all.sh                       # One-click build (charts + mermaid + PDF)
├── generate_charts.py                 # matplotlib charts -> img/
├── number-figures.lua                 # Pandoc filter (section numbering / captions)
├── hsbc-template.latex                # HSBC-branded LaTeX template
├── HSBC-AME-RR-Summary-en.md          # Markdown source (single-file fallback)
├── HSBC-AME-RR-Summary-en.pdf         # (generated) Final PDF
├── chapters/                          # Split chapters for editing (auto-detected)
│   ├── 00-frontmatter.md              #   Title + metadata
│   ├── 01-1-executive-summary.md      #   §1 Executive Summary
│   ├── 02-2-hsbc-ame-market-...       #   §2 Market Coverage
│   ├── 03-3-five-level-...            #   §3 Regulatory Taxonomy
│   ├── 04-4-data-localization-...     #   §4 Data Localisation
│   ├── 05-5-distributed-...           #   §5 Distributed Architecture
│   ├── 06-6-tokenization-...          #   §6 Tokenization & PETs
│   ├── 07-7-implementation-...        #   §7 Priorities & Roadmap
│   ├── 08-8-critical-success-...      #   §8 Critical Success Factors
│   ├── 09-9-references-and-...        #   §9 References & Sources
│   └── 10-appendix.md                 #   Appendix A–E
└── img/
    ├── chart1_business_mix.png        # Python charts
    ├── chart2_size_vs_automation.png
    ├── chart3_reg_intensity.png
    └── mermaid/
        ├── diagram_01.mmd ~ 07.mmd    # Mermaid source (English)
        └── diagram_01.png ~ 07.png    # Mermaid diagrams (rendered)
```

> **Note:** If `chapters/` exists, `build_all.sh` reads from it. Otherwise falls back to `HSBC-AME-RR-Summary-en.md`. Edit individual chapters for easier maintenance; the full PDF is assembled in order.

## Build Pipeline

```
generate_charts.py    build_all.sh (mmdc)    build_all.sh (pandoc)
      │                      │                      │
      │ matplotlib            │ mermaid-cli          │ pandoc + xelatex
      ▼                      ▼                      ▼
  img/chart*.png      img/mermaid/diagram_*.png    .md --> .pdf
                                                   (via number-figures.lua
                                                   + hsbc-template.latex)
```

1. **`generate_charts.py`** — 3 matplotlib charts
2. **`mmdc` (mermaid-cli)** — Renders `img/mermaid/*.mmd` to PNG
3. **`pandoc + xelatex`** — Concatenate chapters → preprocess emoji/Unicode → LaTeX → PDF

## Usage

```bash
./build_all.sh              # Full build (charts + mermaid + PDF)
./build_all.sh --pdf-only   # PDF only (skip charts & mermaid)
./build_all.sh --clean      # Remove build artifacts
```

## Report Contents

| Section | Content |
|---------|---------|
| 1 Executive Summary | Key findings, strategic recommendations |
| 2 Market Coverage | 22 APAC markets, customer matrix, business charts |
| 3 Regulatory Taxonomy | Five-level classification, 14 markets, Islamic finance |
| 4 Data Localisation | Three-tier classification, cross-border rules |
| 5 Distributed Architecture | Five-layer architecture, AML MPC screening |
| 6 Tokenization | Four-layer scheme (FPT/Deterministic/Aggregate/ZKP) |
| 7 Implementation Priorities | Three-phase roadmap, priority matrix |
| 8 Critical Success Factors | 7-factor CSF matrix |
| 9 References | 64 citations |
| Appendix | Penalty cases, standards evolution, regulatory inventory, glossary |

## FAQ

**Build fails with `mmdc: command not found`**
```bash
npm install -g @mermaid-js/mermaid-cli
```

**Chinese characters appear as tofu in PDF**
```bash
brew install --cask font-noto-sans-cjk-sc
```

**Only changed markdown, skip chart & mermaid regeneration**
```bash
./build_all.sh --pdf-only
```

**LaTeX error `\pandocbounded undefined`**

Upgrade pandoc to >= 3.0: `brew upgrade pandoc`
