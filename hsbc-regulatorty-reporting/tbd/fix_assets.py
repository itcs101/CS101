#!/usr/bin/env python3
"""Rename mermaid files to clean names & update all references."""
import os, re, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MERMAID_DIR = os.path.join(SCRIPT_DIR, "img", "mermaid")
MD_FILE = os.path.join(SCRIPT_DIR, "HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.md")
NOTEBOOK = os.path.join(SCRIPT_DIR, "HSBC-APAC-Regulatory-Reporting-Consulting-Report.ipynb")
BUILD_PY = os.path.join(SCRIPT_DIR, "build_report.py")
BUILD_SH = os.path.join(SCRIPT_DIR, "build.sh")

# ── Clean name mapping ──
# (old_pattern, new_base) — order matters (longest match first)
CLEAN_MAP = [
    # old filename fragment (without ext) → new basename
    ("5_4_____AML__________MPC____________3", "diagram_04_aml_mpc_flow"),
    ("5_2____________________2", "diagram_03_distributed_arch"),
    ("2_2________________0", "diagram_01_org_structure"),
    ("2_3________________1", "diagram_02_customer_product"),
    ("5_5_______________4", "diagram_05_prudential_flow"),
    ("6_2_Tokenization________5", "diagram_06_tokenization"),
    ("7_2__________6", "diagram_07_roadmap"),
]

# ── Step 1: Rename files ──
renames = []  # (old_path, new_path)
for old_frag, new_base in CLEAN_MAP:
    for ext in (".png", ".mmd"):
        old_path = os.path.join(MERMAID_DIR, old_frag + ext)
        new_path = os.path.join(MERMAID_DIR, new_base + ext)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            renames.append((old_path, new_path))
            print(f"  {os.path.basename(old_path)} → {os.path.basename(new_path)}")

# ── Step 2: Update references in all files ──
def update_refs(filepath, is_json=False):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    for old_frag, new_base in CLEAN_MAP:
        old_png = f"img/mermaid/{old_frag}.png"
        new_png = f"img/mermaid/{new_base}.png"
        old_mmd = f"img/mermaid/{old_frag}.mmd"
        new_mmd = f"img/mermaid/{new_base}.mmd"
        content = content.replace(old_png, new_png)
        content = content.replace(old_mmd, new_mmd)
        # Also handle the ID references in build_report.py
        content = content.replace(old_frag, new_base)
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Updated: {os.path.basename(filepath)}")

update_refs(MD_FILE)
update_refs(NOTEBOOK)
update_refs(BUILD_PY)
update_refs(BUILD_SH)

# ── Step 3: Verify ──
print("\nFinal mermaid directory:")
for f in sorted(os.listdir(MERMAID_DIR)):
    print(f"  {f}")

# Check no old names remain in markdown
with open(MD_FILE) as f:
    md = f.read()
for old_frag, _ in CLEAN_MAP:
    if old_frag in md:
        print(f"  ⚠️  Old reference still in .md: {old_frag}")

# Count refs
refs = re.findall(r'img/mermaid/[^)]+', md)
print(f"\n  Mermaid refs in .md: {len(refs)}")
for r in refs:
    print(f"    {r}")
