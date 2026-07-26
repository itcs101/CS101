#!/usr/bin/env python3
"""Build the HSBC Regulatory Reporting Report.

Steps:
  1. Read the .ipynb notebook
  2. Extract all mermaid diagrams → .mmd files → render to PNG via mmdc
  3. Replace Python code cells with chart image references
  4. Replace mermaid code blocks with rendered PNG references
  5. Write the final .md ready for pandoc → PDF conversion

Usage:
  python3 build_report.py          # full build
  python3 build_report.py --md-only  # skip mermaid rendering, just produce .md
"""

import json, os, subprocess, sys, re, textwrap, hashlib, base64, zlib

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
NOTEBOOK    = os.path.join(SCRIPT_DIR, "HSBC-APAC-Regulatory-Reporting-Consulting-Report.ipynb")
IMG_DIR     = os.path.join(SCRIPT_DIR, "img")
MERMAID_DIR = os.path.join(IMG_DIR, "mermaid")
OUT_MD      = os.path.join(SCRIPT_DIR, "HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.md")

os.makedirs(MERMAID_DIR, exist_ok=True)

SKIP_MERMAID = "--md-only" in sys.argv

# ═══════════════════════════════════════════════════════════════
# STEP 1: Read notebook
# ═══════════════════════════════════════════════════════════════
with open(NOTEBOOK, encoding="utf-8") as f:
    nb = json.load(f)

# ═══════════════════════════════════════════════════════════════
# STEP 2: Extract mermaid diagrams → render PNGs
# ═══════════════════════════════════════════════════════════════
mermaid_map = {}   # cell_index → (diagram_id, png_path, caption)
mermaid_count = 0

for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "markdown":
        continue
    src = "".join(cell["source"])
    # Find ```mermaid ... ``` blocks
    for match in re.finditer(r"```mermaid\n(.*?)```", src, re.DOTALL):
        diagram = match.group(1).strip()
        # Find preceding header for a human-readable name
        header = "diagram"
        for j in range(i - 1, max(i - 5, -1), -1):
            h_src = "".join(nb["cells"][j]["source"])
            h_m = re.match(r"^#{1,3}\s+(.+)", h_src)
            if h_m:
                header = h_m.group(1).strip().replace(" ", "_").replace("/", "-")[:60]
                break

        # Find caption (the > *caption* line right after the mermaid block)
        caption = ""
        cap_match = re.search(r"```\s*\n>\s*\*(.+?)\*", match.group(0) + src[src.find(match.group(0))+len(match.group(0)):src.find(match.group(0))+len(match.group(0))+200])
        # simpler: look for line starting with > * after the block
        after_block = src[match.end():match.end()+200]
        cap_m = re.match(r"\s*>\s*\*(.+?)\*", after_block)
        if cap_m:
            caption = cap_m.group(1).strip()

        safe_id = f"diagram_{mermaid_count + 1:02d}"
        mmd_path = os.path.join(MERMAID_DIR, f"{safe_id}.mmd")
        png_path_rel = f"img/mermaid/{safe_id}.png"
        png_path_abs = os.path.join(MERMAID_DIR, f"{safe_id}.png")

        # Write .mmd file
        with open(mmd_path, "w", encoding="utf-8") as f_mmd:
            f_mmd.write(diagram)

        mermaid_map[i] = {
            "id": safe_id,
            "mmd": mmd_path,
            "png_rel": png_path_rel,
            "png_abs": png_path_abs,
            "header": header,
            "caption": caption,
            "diagram": diagram,
        }
        mermaid_count += 1

print(f"Found {mermaid_count} mermaid diagrams in notebook.")

# Render each mermaid diagram to PNG
if not SKIP_MERMAID:
    for idx, info in mermaid_map.items():
        print(f"  Rendering: {info['id']} ({info['header'][:60]}) ...")
        try:
            result = subprocess.run(
                ["mmdc", "-i", info["mmd"], "-o", info["png_abs"],
                 "-w", "1200", "-b", "white", "--pdfFit"],
                capture_output=True, text=True, timeout=30,
            )
            if result.returncode != 0:
                print(f"    WARNING: mmdc failed for {info['id']}: {result.stderr[:200]}")
            else:
                print(f"    → {info['png_rel']}")
        except subprocess.TimeoutExpired:
            print(f"    WARNING: mmdc timed out for {info['id']}")
        except FileNotFoundError:
            print("    ERROR: mmdc not found. Install: npm i -g @mermaid-js/mermaid-cli")
            break
else:
    print("  (--md-only: skipping mermaid PNG rendering)")

# ═══════════════════════════════════════════════════════════════
# STEP 3: Assemble final markdown
# ═══════════════════════════════════════════════════════════════
print("\nAssembling final markdown ...")

md_lines = []
CHART_MAP = {
    # chart description keyword → image path
    "business_mix": "img/chart1_business_mix.png",
    "size_vs_automation": "img/chart2_size_vs_automation.png",
    "reg_intensity": "img/chart3_reg_intensity.png",
}

for i, cell in enumerate(nb["cells"]):
    src = "".join(cell["source"])

    if cell["cell_type"] == "code":
        # Replace Python code cells with chart images
        # Use separate ifs (not elif) — one cell may generate multiple charts
        if "Stacked horizontal" in src or "business mix" in src.lower():
            md_lines.append(f"\n![汇丰亚太区主要市场业务结构对比](img/chart1_business_mix.png)\n")
        if "relative_size" in src or "bubble" in src.lower():
            md_lines.append(f"\n![汇丰亚太区各市场: 业务规模 vs 报送自动化率](img/chart2_size_vs_automation.png)\n")
        if "reg_intensity" in src or "fig3" in src:
            md_lines.append(f"\n![汇丰亚太区: 监管报送强度 vs 业务复杂度 vs 数据本地化约束](img/chart3_reg_intensity.png)\n")
        continue

    if cell["cell_type"] == "markdown":
        # Replace mermaid blocks with rendered PNG images
        if i in mermaid_map:
            info = mermaid_map[i]
            png_path = info["png_rel"]
            if os.path.exists(info["png_abs"]):
                # Replace the mermaid code block with image
                src = re.sub(
                    r"```mermaid\n.*?```\s*\n*>\s*\*.*?\*",
                    f"![{info['header']}]({png_path})\n\n> *图: {info['caption'] or info['header']}*",
                    src, flags=re.DOTALL,
                )
                # If the replacement didn't work (caption format different), try simpler
                if "```mermaid" in src:
                    src = re.sub(
                        r"```mermaid\n.*?```",
                        f"![{info['header']}]({png_path})\n\n> *图: {info['caption'] or info['header']}*",
                        src, flags=re.DOTALL,
                    )
            else:
                # Keep mermaid as code block (fallback)
                pass

        md_lines.append(src)

# Write final .md
final_md = "\n".join(md_lines)

# Clean up: remove %matplotlib inline lines (not needed in markdown)
final_md = re.sub(r"%matplotlib inline\n?", "", final_md)
# Clean up: remove empty image references from code cells that were replaced
final_md = re.sub(r"\n{3,}", "\n\n", final_md)
# ── Structural fixes: blank lines before headings & tables ──
lines = final_md.split('\n')
fixed = []
for i, line in enumerate(lines):
    s = line.strip()
    is_heading = bool(re.match(r'^#{1,6}\s', s))
    is_table   = bool(re.match(r'^\|', s))
    prev = fixed[-1].strip() if fixed else ''
    prev_is_table = bool(re.match(r'^\|', prev)) if prev else False
    if is_heading and len(fixed) > 0 and prev != '':
        fixed.append('')
    elif is_table and len(fixed) > 0 and prev != '' and not prev_is_table:
        fixed.append('')
    fixed.append(line)
final_md = '\n'.join(fixed)
final_md = re.sub(r"\n{3,}", "\n\n", final_md)

# ── Add table captions ──
lines = final_md.split('\n')
out = []
in_table = False
heading_for_table = ""
for i, line in enumerate(lines):
    s = line.strip()
    if s.startswith('|') and not re.match(r'^\|[\s\-:|]+$', s):
        if not in_table:
            in_table = True
            for j in range(i-1, max(i-20, -1), -1):
                hm = re.match(r'^#{1,6}\s+(.+)', lines[j])
                if hm:
                    h = hm.group(1).strip()
                    h = re.sub(r'^\d+\.?\d*\.?\d*\s*', '', h)
                    if h and h not in ('核心观点摘要',):
                        heading_for_table = h
                    break
    elif in_table and not s.startswith('|'):
        in_table = False
        if heading_for_table:
            ni = i
            while ni < len(lines) and lines[ni].strip() == '':
                ni += 1
            if ni >= len(lines) or not lines[ni].strip().startswith(':'):
                out.append('')
                out.append(': ' + heading_for_table)
                out.append('')
        heading_for_table = ""
    out.append(line)
final_md = '\n'.join(out)
final_md = re.sub(r"\n{3,}", "\n\n", final_md)
final_md = final_md.replace("$$$$$", "Very High")
final_md = final_md.replace("$$$$", "Very High")
final_md = final_md.replace("$$$", "High")
final_md = final_md.replace("$$", "Medium")

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write(final_md)

print(f"  Final markdown written: {OUT_MD}")

# Stats
img_refs = len(re.findall(r"!\[.*?\]\(img/", final_md))
mmd_blocks = len(re.findall(r"```mermaid", final_md))
print(f"  Image references: {img_refs}")
print(f"  Remaining mermaid blocks: {mmd_blocks}")

# ═══════════════════════════════════════════════════════════════
# STEP 4: Print next steps
# ═══════════════════════════════════════════════════════════════
print(f"""
╔══════════════════════════════════════════════════════════════╗
║  Build complete!                                            ║
║                                                             ║
║  Next: build PDF                                            ║
║    cd {SCRIPT_DIR}                                         ║
║    ./build.sh "{OUT_MD}"                                   ║
║                                                             ║
║  Charts:  {SCRIPT_DIR}/img/                         ║
║  Mermaid: {SCRIPT_DIR}/img/mermaid/                  ║
╚══════════════════════════════════════════════════════════════╝
""")
