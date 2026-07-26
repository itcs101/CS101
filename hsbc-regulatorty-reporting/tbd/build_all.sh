#!/bin/bash
#=============================================================================
#  build_all.sh — HSBC APAC Regulatory Reporting: Build Pipeline
#  Generates Python charts (optional), then Markdown → PDF via pandoc + xelatex.
#  No .ipynb dependency — works directly from the .md file.
#
#  Usage:
#    ./build_all.sh              # full build (charts + PDF)
#    ./build_all.sh --pdf-only   # skip charts, only build PDF
#    ./build_all.sh --clean      # remove build artifacts
#=============================================================================
set -euo pipefail
cd "$(dirname "$0")"

MDFILE="HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.md"
PDFFILE="HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.pdf"

case "${1:-}" in
    --clean)
        echo "Cleaning..."
        rm -f /tmp/hsbc-build.md
        rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk
        echo "✅ Clean."
        exit 0
        ;;
    --pdf-only)
        echo "Skipping chart generation..."
        ;;
    *)
        echo "=== Step 1/3: Generating Python charts ==="
        python3 generate_charts.py
        echo ""
        ;;
esac

echo "=== Building PDF ==="
# Preprocess: emoji → LaTeX, flag emoji → ISO codes
python3 << 'PYEOF'
import re
with open("HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.md") as f:
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

pandoc /tmp/hsbc-build.md \
    --lua-filter=number-figures.lua \
    --template=hsbc-template.latex \
    --pdf-engine=xelatex \
    --toc --toc-depth=2 --number-sections \
    --metadata date="2026年7月25日" \
    --metadata author="亚太区监管报送专家顾问组" \
    --no-highlight \
    --resource-path="." \
    -o "$PDFFILE"

echo ""
ls -lh "$PDFFILE"
echo "✅ Build complete."
