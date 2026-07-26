#!/usr/bin/env bash
#=============================================================================
#  build.sh — HSBC APAC Regulatory Reporting Report PDF Builder
#  Converts the FINAL markdown report to a professionally-styled PDF using
#  pandoc + xelatex with the HSBC-branded LaTeX template.
#
#  Usage:
#    ./build.sh                           # build HSBC-APAC-...-FINAL.md → PDF
#    ./build.sh <input.md>                # build arbitrary .md file
#    ./build.sh --clean                   # remove build artifacts
#
#  Dependencies: pandoc, xelatex (TeX Live / MacTeX)
#=============================================================================

set -euo pipefail

# --- Configuration -----------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="${SCRIPT_DIR}/hsbc-template.latex"
DEFAULT_INPUT="${SCRIPT_DIR}/HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.md"

# HSBC brand styling
HSBC_RED='\033[0;31m'
HSBC_DARK='\033[0;90m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# --- Detect TeX Live / MacTeX -------------------------------------------------
detect_tex_distro() {
    if command -v kpsewhich &>/dev/null; then
        kpsewhich --var-value=TEXMFDIST 2>/dev/null || echo ""
    else
        echo ""
    fi
}

# Can we find an available CJK font on this machine?
detect_cjk_fonts() {
    local available=""

    # Method 1: fc-list (Linux, Homebrew fontconfig on macOS)
    if command -v fc-list &>/dev/null && fc-list :lang=zh 2>/dev/null | grep -q .; then
        if fc-list :lang=zh 2>/dev/null | grep -qi "Noto.*CJK"; then
            available="Noto Sans CJK SC"
        elif fc-list :lang=zh 2>/dev/null | grep -qi "Source Han"; then
            available="Source Han Sans SC"
        elif fc-list :lang=zh 2>/dev/null | grep -qi "Fandol"; then
            available="FandolSong"
        elif fc-list :lang=zh 2>/dev/null | grep -qi "SimSun\|宋体\|SimHei"; then
            available="SimSun"
        fi
    fi

    # Method 2: macOS system_profiler (macOS font registry)
    if [[ -z "$available" ]] && command -v system_profiler &>/dev/null; then
        if system_profiler SPFontsDataType 2>/dev/null | grep -qi "PingFang"; then
            available="PingFang SC (Apple system font)"
        fi
    fi

    # Method 3: Check for PingFang font files directly
    if [[ -z "$available" ]]; then
        if ls /System/Library/Fonts/PingFang* &>/dev/null 2>&1 || \
           ls /System/Library/AssetsV2/*/AssetData/PingFang* &>/dev/null 2>&1; then
            available="PingFang SC (Apple system font)"
        fi
    fi

    echo "$available"
}

# --- Help --------------------------------------------------------------------
usage() {
    cat <<EOF
${BOLD}HSBC APAC Regulatory Reporting — PDF Build Script${NC}

Usage:
  ./build.sh                     Build the default FINAL report → PDF
  ./build.sh <input-file.md>     Build a specific markdown file → PDF
  ./build.sh --clean             Remove build artifacts (*.aux, *.log, etc.)
  ./build.sh --help              Show this help message

Dependencies:
  pandoc ≥ 2.0          Markdown → LaTeX converter
  xelatex                XeLaTeX engine (from TeX Live / MacTeX)
  Noto CJK fonts         Recommended: noto-cjk (or Source Han Sans)
  LaTeX packages         fontspec, xeCJK, xcolor, booktabs, fancyvrb,
                         tcolorbox, titlesec, scrlayer-scrpage, tikz,
                         caption, hyperref, enumitem, framed, longtable,
                         multirow, colortbl, geometry, csquotes

Font installation (macOS):
  brew install --cask font-noto-sans-cjk-sc font-noto-sans-mono

Font installation (Ubuntu/Debian):
  sudo apt install fonts-noto-cjk fonts-noto-cjk-extra
EOF
    exit 0
}

# --- Cleanup -----------------------------------------------------------------
do_clean() {
    local dir="${1:-$SCRIPT_DIR}"
    echo -e "${HSBC_DARK}Cleaning build artifacts...${NC}"
    rm -f "${dir}"/*.aux "${dir}"/*.log "${dir}"/*.out "${dir}"/*.toc \
          "${dir}"/*.synctex.gz "${dir}"/*.bbl "${dir}"/*.blg \
          "${dir}"/*.run.xml "${dir}"/*-blx.bib "${dir}"/*.bcf \
          "${dir}"/*.nav "${dir}"/*.snm "${dir}"/*.vrb \
          "${dir}"/*.pyg "${dir}"/*.lol "${dir}"/*.lof "${dir}"/*.lot \
          "${dir}"/*.fdb_latexmk "${dir}"/*.fls \
          "${dir}"/texput.log 2>/dev/null || true
    echo -e "  ${HSBC_RED}✓${NC} Done."
}

# --- Pre-flight checks -------------------------------------------------------
check_dependencies() {
    local missing=()

    if ! command -v pandoc &>/dev/null; then
        missing+=("pandoc")
    fi

    if ! command -v xelatex &>/dev/null; then
        missing+=("xelatex (TeX Live / MacTeX)")
    fi

    if [[ ${#missing[@]} -gt 0 ]]; then
        echo -e "${HSBC_RED}ERROR: Missing required dependencies:${NC}"
        for dep in "${missing[@]}"; do
            echo -e "  • $dep"
        done
        echo ""
        echo "Installation instructions:"
        echo "  macOS:  brew install pandoc mactex-no-gui"
        echo "  Ubuntu: sudo apt install pandoc texlive-xetex texlive-latex-extra"
        echo ""
        echo "After installing TeX, install CJK fonts:"
        echo "  macOS:  brew install --cask font-noto-sans-cjk-sc font-noto-sans-mono"
        exit 1
    fi

    # Check for CJK fonts (non-blocking — template has font fallback logic)
    local cjk_font
    cjk_font=$(detect_cjk_fonts)
    if [[ -z "$cjk_font" ]]; then
        echo -e "${HSBC_RED}WARNING: No CJK font detected by fc-list/system_profiler.${NC}"
        echo "  The LaTeX template will attempt to use PingFang SC (macOS)"
        echo "  or Noto Sans CJK SC (Linux) via IfFontExistsTF fallback."
        echo "  If PDF renders without Chinese text, install:"
        echo "    brew install --cask font-noto-sans-cjk-sc"
        echo ""
    else
        echo -e "  CJK font: ${HSBC_DARK}${cjk_font}${NC}"
    fi

    # Check template exists
    if [[ ! -f "$TEMPLATE" ]]; then
        echo -e "${HSBC_RED}ERROR: LaTeX template not found:${NC} $TEMPLATE"
        exit 1
    fi
}

# --- Build PDF ---------------------------------------------------------------
build_pdf() {
    local input_md="$1"
    local output_pdf="${input_md%.md}.pdf"
    local basename
    basename="$(basename "${input_md%.md}")"
    local tmp_md
    tmp_md="$(mktemp /tmp/hsbc-build-XXXXXXXX.md)"

    echo ""
    echo -e "${HSBC_RED}${BOLD}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${HSBC_RED}${BOLD}║     HSBC APAC Regulatory Reporting — PDF Build Pipeline      ║${NC}"
    echo -e "${HSBC_RED}${BOLD}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "  Input:    ${HSBC_DARK}${input_md}${NC}"
    echo -e "  Output:   ${HSBC_DARK}${output_pdf}${NC}"
    echo -e "  Template: ${HSBC_DARK}${TEMPLATE}${NC}"
    echo ""

    # Step 0: Preprocess Markdown — replace emoji with LaTeX commands
    #  Apple Color Emoji is a sbix bitmap font unsupported by xelatex.
    #  These Unicode chars are missing from PingFang SC / Noto CJK as well,
    #  so we replace them with LaTeX \hsbc* commands defined in the template.
    echo -e "${BOLD}[1/4]${NC} Preprocessing Markdown (emoji → LaTeX macros) ..."

    # Use Python for reliable multi-byte Unicode replacement
    python3 -c "
import sys, re
text = open('$input_md', 'r', encoding='utf-8').read()
# Flag emoji → ISO codes (avoid monospace font missing-char warnings)
for flag, iso in [
    ('\U0001f1ed\U0001f1f0','HK'),('\U0001f1e8\U0001f1f3','CN'),
    ('\U0001f1f9\U0001f1fc','TW'),('\U0001f1f2\U0001f1f4','MO'),
    ('\U0001f1f8\U0001f1ec','SG'),('\U0001f1f2\U0001f1fe','MY'),
    ('\U0001f1ee\U0001f1e9','ID'),('\U0001f1f9\U0001f1ed','TH'),
    ('\U0001f1fb\U0001f1f3','VN'),('\U0001f1f5\U0001f1ed','PH'),
    ('\U0001f1ee\U0001f1f3','IN'),('\U0001f1ef\U0001f1f5','JP'),
    ('\U0001f1f0\U0001f1f7','KR'),('\U0001f1e6\U0001f1fa','AU'),
    ('\U0001f1f3\U0001f1ff','NZ'),
]: text = text.replace(flag, iso)
# Emoji → LaTeX macros
text = text.replace('⭐', r'\hsbcstar{}')
text = text.replace('\U0001f534', r'\hsbcredball{}')
text = text.replace('✅', r'\hsbccheck{}')
text = text.replace('❌', r'\hsbccross{}')
text = text.replace('\U0001f6ab', r'\hsbcprohibit{}')
text = text.replace('⚠️', r'\hsbcwarn{}')
text = text.replace('⚠', r'\hsbcwarn{}')
# Cost indicators → text (avoid LaTeX math-mode errors)
text = text.replace('\$\$\$\$\$', 'Very High')
text = text.replace('\$\$\$\$', 'Very High')
text = text.replace('\$\$\$', 'High')
text = text.replace('\$\$', 'Medium')
# Unicode chars missing from CJK fonts
text = text.replace('◐', '~')
text = text.replace('\U0001f7e0', r'\textcolor{orange}{\textbullet}')
text = text.replace('\U0001f7e1', r'\textcolor{hsbcgold}{\textbullet}')
text = text.replace('\U0001f7e2', r'\textcolor{hsbcgreen}{\textbullet}')
open('$tmp_md', 'w', encoding='utf-8').write(text)
" 2>&1

    echo -e "  ${HSBC_RED}✓${NC} Preprocessing complete."

    # Step 1: Pandoc MD → PDF (single pass with xelatex)
    echo ""
    echo -e "${BOLD}[2/4]${NC} Converting Markdown → PDF via pandoc + xelatex ..."
    echo ""

    pandoc "$tmp_md" \
        --from=markdown+grid_tables+pipe_tables+multiline_tables+raw_attribute+fenced_divs+bracketed_spans+fancy_lists+startnum+definition_lists \
        --to=latex \
        --template="$TEMPLATE" \
        --pdf-engine=xelatex \
        --no-highlight \
        --resource-path="$(dirname "$input_md")" \
        --toc \
        --toc-depth=2 \
        --number-sections \
        --shift-heading-level-by=0 \
        --top-level-division=section \
        --metadata date="2026年7月25日" \
        --metadata author="亚太区监管报送专家顾问组" \
        --variable=links-as-notes \
        --variable=colorlinks \
        --variable=toc:true \
        -o "$output_pdf" \
        2>&1 | tail -20

    # Clean up temp file
    rm -f "$tmp_md"

    echo ""

    # Step 2: Clean auxiliary files
    echo -e "${BOLD}[3/4]${NC} Cleaning LaTeX auxiliary files ..."
    do_clean "$SCRIPT_DIR"

    # Step 3: Summary
    echo ""
    if [[ -f "$output_pdf" ]]; then
        local filesize
        filesize=$(du -h "$output_pdf" | cut -f1)
        local pages
        if command -v pdfinfo &>/dev/null; then
            pages=$(pdfinfo "$output_pdf" 2>/dev/null | awk '/^Pages:/{print $2}' || echo "?")
        elif command -v mdls &>/dev/null; then
            pages=$(mdls -name kMDItemNumberOfPages -raw "$output_pdf" 2>/dev/null || echo "?")
        elif command -v python3 &>/dev/null; then
            pages=$(python3 -c "
import re
with open('$output_pdf', 'rb') as f:
    content = f.read()
    matches = re.findall(rb'/Type\s*/Page[^s]', content)
    print(len(matches))
" 2>/dev/null || echo "?")
        else
            pages="?"
        fi

        echo -e "${BOLD}[4/4]${NC} ${HSBC_RED}✓ Build complete!${NC}"
        echo ""
        echo -e "  ${BOLD}Output:${NC}  ${output_pdf}"
        echo -e "  ${BOLD}Size:${NC}    ${filesize}"
        echo -e "  ${BOLD}Pages:${NC}   ${pages}"
        echo ""
        echo -e "  Open with: ${HSBC_DARK}open \"${output_pdf}\"${NC}"
    else
        echo -e "${HSBC_RED}ERROR: PDF was not generated. Check logs above.${NC}"
        rm -f "$tmp_md"
        exit 1
    fi
}

# --- Main --------------------------------------------------------------------
main() {
    case "${1:-}" in
        --help|-h|help)
            usage
            ;;
        --clean)
            do_clean "$SCRIPT_DIR"
            exit 0
            ;;
        "")
            # Default: build the FINAL report
            if [[ ! -f "$DEFAULT_INPUT" ]]; then
                echo -e "${HSBC_RED}ERROR: Default input not found:${NC} $DEFAULT_INPUT"
                echo "  Usage: ./build.sh <input-file.md>"
                exit 1
            fi
            check_dependencies
            build_pdf "$DEFAULT_INPUT"
            ;;
        *)
            if [[ ! -f "$1" ]]; then
                echo -e "${HSBC_RED}ERROR: Input file not found:${NC} $1"
                exit 1
            fi
            check_dependencies
            build_pdf "$1"
            ;;
    esac
}

main "$@"
