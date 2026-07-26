#!/bin/bash
#=============================================================================
#  build_all.sh — HSBC APAC Regulatory Reporting: Build Pipeline
#  Generates Python charts (optional), then Markdown → PDF via pandoc + xelatex.
#  No .ipynb dependency — works directly from the .md file.
#
#  Usage:
#    ./build_all.sh              # full build (charts + mermaid + PDF)
#    ./build_all.sh --pdf-only   # skip charts & mermaid, only build PDF
#    ./build_all.sh --clean      # remove build artifacts
#=============================================================================
set -euo pipefail
cd "$(dirname "$0")/.."

MDFILE="HSBC-AME-RR-summary-cn.md"
PDFFILE="pdf/HSBC-AME-RR-summary-cn.pdf"

case "${1:-}" in
    --clean)
        echo "Cleaning..."
        rm -f /tmp/hsbc-build.md
        rm -f pdf/*.aux pdf/*.log pdf/*.out pdf/*.toc pdf/*.synctex.gz pdf/*.fls pdf/*.fdb_latexmk
        echo "✅ Clean."
        exit 0
        ;;
    --pdf-only)
        echo "Skipping chart + mermaid generation..."
        MMD_SKIP=1
        ;;
    *)
        echo "=== Step 1/3: Generating Python charts ==="
        python3 script/generate_charts.py
        echo ""
        ;;
esac

if [[ -z "${MMD_SKIP:-}" ]]; then
    echo "=== Rendering Mermaid diagrams ==="
    MMD_DIR="chapters/img/mermaid"
    for f in "$MMD_DIR"/diagram_0?.mmd; do
        out="${f%.mmd}.png"
        echo "  $(basename "$f") → $(basename "$out")"
        mmdc -i "$f" -o "$out" -b white -s 2
    done
    echo ""
fi

echo "=== Building PDF ==="
# Preprocess: emoji → LaTeX, flag emoji → ISO codes,
# ensure blank lines before pipe tables (pandoc spec requirement)
python3 << 'PYEOF'
import re, os, glob
t = ""
chap_dir = "chapters"
if os.path.isdir(chap_dir):
    for f in sorted(glob.glob(f"{chap_dir}/*.md")):
        with open(f) as fp:
            t += fp.read() + "\n"
else:
    with open("HSBC-AME-RR-summary-cn.md") as f:
        t = f.read()
for fg, iso in [('🇭🇰','HK'),('🇨🇳','CN'),('🇹🇼','TW'),('🇲🇴','MO'),('🇸🇬','SG'),
    ('🇲🇾','MY'),('🇮🇩','ID'),('🇹🇭','TH'),('🇻🇳','VN'),('🇵🇭','PH'),
    ('🇮🇳','IN'),('🇯🇵','JP'),('🇰🇷','KR'),('🇦🇺','AU'),('🇳🇿','NZ')]:
    t = t.replace(fg, iso)
for e, c in [('⭐','\\hsbcstar{}'),('✅','\\hsbccheck{}'),('❌','\\hsbccross{}'),
    ('⚠️','\\hsbcwarn{}'),('⚠','\\hsbcwarn{}'),('🚫','\\hsbcprohibit{}'),
    ('🔴','\\hsbcredball{}'),('◐','~'),
    ('🟠','\\textcolor{orange}{\\textbullet}'),
    ('🟡','\\textcolor{hsbcgold}{\\textbullet}'),
    ('🟢','\\textcolor{hsbcgreen}{\\textbullet}')]:
    t = t.replace(e, c)
t = re.sub(r'\n> \*图[^:]*:.*?\*\n', '\n', t)
open('/tmp/hsbc-build.md', 'w').write(t)
print("  Preprocessed")
PYEOF

# Generate LaTeX first, then fix alignment, then compile to PDF
TEXFILE="/tmp/hsbc-build.tex"
pandoc /tmp/hsbc-build.md \
    --lua-filter=script/number-figures.lua \
    --template=latex/hsbc-template.latex \
    --toc --toc-depth=2 --number-sections \
    --metadata date="2026年7月25日" \
    --metadata author="亚太区监管报送专家顾问组" \
    --no-highlight \
    --resource-path=".:chapters" \
    -o "$TEXFILE"

# Replace \raggedright with \centering for proper table cell alignment
sed -i '' 's/\\raggedright/\\centering/g' "$TEXFILE"
sed -i '' 's/\\raggedleft/\\centering/g' "$TEXFILE"

# Compile LaTeX to PDF
xelatex -interaction=nonstopmode -output-directory="$(dirname "$TEXFILE")" "$TEXFILE" > /dev/null 2>&1
xelatex -interaction=nonstopmode -output-directory="$(dirname "$TEXFILE")" "$TEXFILE" > /dev/null 2>&1
cp "$(dirname "$TEXFILE")/$(basename "$TEXFILE" .tex).pdf" "$PDFFILE"

echo ""
ls -lh "$PDFFILE"
echo "✅ Build complete."
