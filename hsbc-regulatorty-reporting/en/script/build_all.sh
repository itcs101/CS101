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

MDFILE="HSBC-AME-RR-Summary-en.md"
PDFFILE="pdf/HSBC-AME-RR-Summary-en.pdf"

case "${1:-}" in
    --clean)
        echo "Cleaning..."
        rm -f /tmp/hsbc-build.md
        rm -f pdf/*.aux pdf/*.log pdf/*.out pdf/*.toc pdf/*.synctex.gz pdf/*.fls pdf/*.fdb_latexmk
        echo "Done."
        exit 0
        ;;
    --pdf-only)
        echo "Skipping chart + mermaid generation..."
        MMD_SKIP=1
        ;;
    *)
        echo "=== Generating Python charts ==="
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
# Preprocess: emoji → LaTeX, flag emoji → ISO codes
python3 << 'PYEOF'
import re, os, glob
t = ""
chap_dir = "chapters"
if os.path.isdir(chap_dir):
    for f in sorted(glob.glob(f"{chap_dir}/*.md")):
        with open(f) as fp:
            t += fp.read() + "\n"
else:
    with open("HSBC-AME-RR-Summary-en.md") as f:
        t = f.read()
for fg, iso in [('🇭🇰','HK'),('🇨🇳','CN'),('🇹🇼','TW'),('🇲🇴','MO'),('🇸🇬','SG'),
    ('🇲🇾','MY'),('🇮🇩','ID'),('🇹🇭','TH'),('🇻🇳','VN'),('🇵🇭','PH'),
    ('🇮🇳','IN'),('🇯🇵','JP'),('🇰🇷','KR'),('🇦🇺','AU'),('🇳🇿','NZ')]:
    t = t.replace(fg, iso)
for e, c in [('⭐','\\hsbcstar{}'),('✅','\\hsbccheck{}'),('❌','\\hsbccross{}'),('★','$\\bigstar$'),('⚪','$\\circ$'),
    ('⚠️','\\hsbcwarn{}'),('⚠','\\hsbcwarn{}'),('🚫','\\hsbcprohibit{}'),
    ('🔴','\\hsbcredball{}'),('◐','~'),
    ('🟠','\\textcolor{orange}{\\textbullet}'),
    ('🟡','\\textcolor{hsbcgold}{\\textbullet}'),
    ('🟢','\\textcolor{hsbcgreen}{\\textbullet}')]:
    t = t.replace(e, c)
# Remove redundant blockquote captions (filter adds proper numbered captions)
t = re.sub(r'\n> \*(?:图|Figure)[^:]*:.*?\*\n', '\n', t)
open('/tmp/hsbc-build.md', 'w').write(t)
print("  Preprocessed")
PYEOF

pandoc /tmp/hsbc-build.md \
    --lua-filter=script/number-figures.lua \
    --template=latex/hsbc-template.latex \
    --pdf-engine=xelatex \
    --toc --toc-depth=2 --number-sections \
    --metadata date="July 25, 2026" \
    --metadata author="APAC Regulatory Reporting Advisory Panel" \
    --no-highlight \
    --resource-path=".:chapters" \
    -o "$PDFFILE"

echo ""
ls -lh "$PDFFILE"
echo "Build complete."
