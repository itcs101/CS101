# HSBC APAC Regulatory Reporting — Build Pipeline
# Usage: make          (generate charts, then markdown → PDF)
#        make charts   (only regenerate Python charts)
#        make clean    (remove build artifacts)

.PHONY: all charts pdf clean

all: charts pdf

# ── Step 1: Generate Python charts (matplotlib) ──
charts:
	python3 generate_charts.py

# ── Step 2: Render mermaid diagrams + assemble markdown ──
build/markdown:
	python3 build_report.py

# ── Step 3: Preprocess + pandoc + xelatex → PDF ──
pdf: build/markdown
	@echo "=== Building PDF ==="
	python3 -c "
import re
with open('HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.md') as f:
    t = f.read()
# Flag emoji → ISO
for fg,iso in [('\U0001f1ed\U0001f1f0','HK'),('\U0001f1e8\U0001f1f3','CN'),('\U0001f1f9\U0001f1fc','TW'),('\U0001f1f2\U0001f1f4','MO'),('\U0001f1f8\U0001f1ec','SG'),('\U0001f1f2\U0001f1fe','MY'),('\U0001f1ee\U0001f1e9','ID'),('\U0001f1f9\U0001f1ed','TH'),('\U0001f1fb\U0001f1f3','VN'),('\U0001f1f5\U0001f1ed','PH'),('\U0001f1ee\U0001f1f3','IN'),('\U0001f1ef\U0001f1f5','JP'),('\U0001f1f0\U0001f1f7','KR'),('\U0001f1e6\U0001f1fa','AU'),('\U0001f1f3\U0001f1ff','NZ')]:
    t=t.replace(fg,iso)
# Emoji → LaTeX
for e,c in [('⭐','\\\\hsbcstar{}'),('✅','\\\\hsbccheck{}'),('❌','\\\\hsbccross{}'),('⚠️','\\\\hsbcwarn{}'),('⚠','\\\\hsbcwarn{}'),('🚫','\\\\hsbcprohibit{}'),('🔴','\\\\hsbcredball{}'),('◐','~'),('🟠','\\\\textcolor{orange}{\\\\textbullet}'),('🟡','\\\\textcolor{hsbcgold}{\\\\textbullet}'),('🟢','\\\\textcolor{hsbcgreen}{\\\\textbullet}')]:
    t=t.replace(e,c)
t=re.sub(r'\n> \*图[^:]*:.*?\*\n','\n',t)
open('/tmp/hsbc-build.md','w').write(t)
print('  Preprocessed')
"
	pandoc /tmp/hsbc-build.md \
		--lua-filter=number-figures.lua \
		--template=hsbc-template.latex \
		--pdf-engine=xelatex \
		--toc --toc-depth=2 --number-sections \
		--metadata date="2026年7月25日" \
		--metadata author="亚太区监管报送专家顾问组" \
		--no-highlight \
		--resource-path="." \
		-o "HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.pdf"
	@echo ""
	@ls -lh HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.pdf
	@echo "✅ Done."

clean:
	rm -f /tmp/hsbc-build.md /tmp/hsbc-preproc.md /tmp/hsbc-final.md /tmp/hsbc-*.tex /tmp/hsbc-*.pdf
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk
	@echo "✅ Cleaned."
