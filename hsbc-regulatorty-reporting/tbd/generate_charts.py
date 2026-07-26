#!/usr/bin/env python3
"""Generate charts for HSBC APAC Regulatory Reporting Report.
   Saves PNGs to ./img/ with proper Chinese font rendering on macOS.
   Usage: python3 generate_charts.py
"""

import os, warnings
import matplotlib
matplotlib.use("Agg")  # headless rendering — no display needed
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as mticker
import numpy as np
from matplotlib.lines import Line2D

# Suppress font fallback warnings — we handle CJK explicitly
warnings.filterwarnings("ignore", message="Glyph.*missing from font")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(IMG_DIR, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# FONT SETUP — find a CJK-capable font on this system
# ═══════════════════════════════════════════════════════════════
def find_cjk_font():
    """Return a font name that supports Chinese glyphs, preferring PingFang SC."""
    candidates = [
        "PingFang SC", "STHeiti", "Heiti SC", "Heiti TC",
        "Hiragino Sans GB", "Hiragino Sans CNS",
        "Noto Sans CJK SC", "Noto Sans SC",
        "Source Han Sans SC", "SimHei",
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            return name
    # fallback: scan font files for "SC" or "CJK"
    for f in fm.fontManager.ttflist:
        if "PingFang" in f.name:
            return f.name
        if "Heiti" in f.name:
            return f.name
    return None

CJK_FONT = find_cjk_font()
print(f"CJK Font: {CJK_FONT}")

if CJK_FONT:
    plt.rcParams["font.family"]      = "sans-serif"
    plt.rcParams["font.sans-serif"]  = [CJK_FONT, "DejaVu Sans", "Arial"]
    plt.rcParams["axes.unicode_minus"] = False
else:
    print("WARNING: No CJK font found — Chinese labels may render as tofu (□□□).")
    print("  Install: brew install --cask font-noto-sans-cjk-sc")

# ═══════════════════════════════════════════════════════════════
# DATA — estimated from HSBC public disclosures (2025 Annual Report, market websites)
# ═══════════════════════════════════════════════════════════════
HSBC_RED   = "#DB0011"
HSBC_BLUE  = "#2E5090"
HSBC_GOLD  = "#FFB81C"
HSBC_GREEN = "#00A86B"
HSBC_GREY  = "#666666"
HSBC_DARK  = "#333333"
HSBC_LIGHT = "#F5F5F5"

MARKETS = [
    "香港", "中国大陆", "台湾", "新加坡", "马来西亚", "澳大利亚",
    "印度", "印尼", "日本", "韩国", "泰国", "越南", "菲律宾", "新西兰",
]

# Business mix (%): retail, corporate, wealth, islamic
RETAIL    = [35, 15, 30, 20, 25, 35, 20, 10,  0, 10,  0, 30, 40, 55]
CORPORATE = [40, 50, 40, 45, 45, 40, 50, 60, 80, 90, 80, 70, 60, 25]
WEALTH    = [25, 35, 30, 35, 20, 25, 30, 30, 20,  0, 20,  0,  0, 20]
ISLAMIC   = [ 0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0]

# Relative business size (HK = 100), automation rate (%)
REL_SIZE  = [100, 45, 18, 35, 22, 20, 16, 12, 8, 7, 6, 8, 6, 10]
AUTOMATION = [92, 75, 45, 88, 55, 78, 50, 40, 35, 30, 42, 38, 45, 50]

# Regulation intensity, business complexity, data localisation tier
REG_INTENSITY   = [95, 90, 88, 88, 78, 82, 70, 72, 92, 95, 65, 68, 60, 75]
BIZ_COMPLEXITY  = [95, 82, 75, 85, 80, 70, 65, 60, 55, 62, 50, 52, 48, 58]
DATA_LOCAL_TIER = [0, 100, 100, 100, 100, 60, 60, 100, 60, 100, 60, 100, 60, 100]
# Tier: 100 = strong local-storage mandate, 60 = local copy required, 0 = free flow

# ═══════════════════════════════════════════════════════════════
# HELPER: style clean-up
# ═══════════════════════════════════════════════════════════════
def cleanup_ax(ax):
    """Remove chartjunk — top & right spines, light grid."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(HSBC_GREY)
    ax.spines["bottom"].set_color(HSBC_GREY)
    ax.tick_params(colors=HSBC_GREY, which="both")
    ax.grid(True, alpha=0.15, linestyle="--", axis="x")

def save(fig, name):
    path = os.path.join(IMG_DIR, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white", edgecolor="none")
    print(f"  Saved: {path}")
    plt.close(fig)

# ═══════════════════════════════════════════════════════════════
# CHART 1 — Stacked horizontal bar: business mix by market
# ═══════════════════════════════════════════════════════════════
print("\n[1/3] Business mix by market ...")
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

y = np.arange(len(MARKETS))
ax.barh(y, RETAIL,                     color=HSBC_RED,   label="零售银行 Retail")
ax.barh(y, CORPORATE, left=RETAIL,     color=HSBC_BLUE,  label="对公/企业银行 Corporate")
left2 = [r + c for r, c in zip(RETAIL, CORPORATE)]
ax.barh(y, WEALTH,    left=left2,      color="#FFB81C",  label="财富管理 Wealth")
left3 = [l + w for l, w in zip(left2, WEALTH)]
ax.barh(y, ISLAMIC,   left=left3,      color=HSBC_GREEN, label="伊斯兰金融 Islamic")

for i, (r, c, w, isl) in enumerate(zip(RETAIL, CORPORATE, WEALTH, ISLAMIC)):
    total = r + c + w + isl
    ax.text(total + 1.5, i, f"{total}%", va="center", fontsize=8, color=HSBC_GREY)

ax.set_yticks(y)
ax.set_yticklabels(MARKETS, fontsize=10)
ax.set_xlabel("业务占比 (%)", fontsize=11, color=HSBC_GREY)
ax.set_title("汇丰亚太区主要市场业务结构对比", fontsize=15,
             fontweight="bold", color=HSBC_RED, pad=16)
ax.legend(loc="lower right", fontsize=9, ncol=4, frameon=False)
ax.set_xlim(0, 115)
ax.invert_yaxis()
cleanup_ax(ax)
save(fig, "chart1_business_mix.png")

# ═══════════════════════════════════════════════════════════════
# CHART 2 — Bubble chart: business size vs automation rate
# ═══════════════════════════════════════════════════════════════
print("[2/3] Business size vs automation rate ...")
fig, ax = plt.subplots(figsize=(14, 7.5))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Color by tier: flagship (HK), major, growth, niche
def color_for(m, s, a):
    if s > 50:
        return HSBC_RED
    if s > 15:
        return HSBC_BLUE
    return HSBC_GREY

colors = [color_for(m, s, a) for m, s, a in zip(MARKETS, REL_SIZE, AUTOMATION)]
sizes  = [max(s * 10, 40) for s in REL_SIZE]

ax.scatter(REL_SIZE, AUTOMATION, s=sizes, c=colors, alpha=0.85,
           edgecolors="white", linewidth=1.2, zorder=3)

for i, mkt in enumerate(MARKETS):
    offset_y = 2.2 if i % 2 == 0 else -3.0
    ax.annotate(mkt, (REL_SIZE[i], AUTOMATION[i]),
                textcoords="offset points", xytext=(0, offset_y),
                fontsize=8.5, ha="center", color=HSBC_DARK,
                zorder=4)

ax.axhline(y=60, color=HSBC_RED, linestyle="--", alpha=0.4, linewidth=1.2)
ax.text(REL_SIZE[0] + 2, 61, "当前平均 ~60%", fontsize=8, color=HSBC_RED, va="bottom")
ax.axhline(y=90, color=HSBC_GREEN, linestyle="--", alpha=0.4, linewidth=1.2)
ax.text(REL_SIZE[0] + 2, 91, "目标  90%+", fontsize=8, color=HSBC_GREEN, va="bottom")

ax.set_xlabel("相对业务规模 (香港 = 100)", fontsize=11, color=HSBC_GREY)
ax.set_ylabel("报送自动化率 (%)", fontsize=11, color=HSBC_GREY)
ax.set_title("汇丰亚太区各市场: 业务规模 vs 报送自动化率", fontsize=15,
             fontweight="bold", color=HSBC_RED, pad=16)

# Custom legend
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=HSBC_RED,  markersize=14, label='旗舰市场 (香港)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=HSBC_BLUE, markersize=12, label='主要市场'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=HSBC_GREY, markersize=9,  label='其他市场'),
    Line2D([0], [0], color=HSBC_RED,  linestyle='--', linewidth=1.2, label='当前平均自动化率 (~60%)'),
    Line2D([0], [0], color=HSBC_GREEN, linestyle='--', linewidth=1.2, label='目标自动化率 (90%+)'),
]
ax.legend(handles=legend_elements, fontsize=8.5, loc="lower right", frameon=False)
cleanup_ax(ax)
save(fig, "chart2_size_vs_automation.png")

# ═══════════════════════════════════════════════════════════════
# CHART 3 — Grouped bar: regulation intensity vs business complexity
# ═══════════════════════════════════════════════════════════════
print("[3/3] Regulation intensity vs business complexity ...")
fig, ax = plt.subplots(figsize=(15, 8))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

x = np.arange(len(MARKETS))
width = 0.35

bars1 = ax.bar(x - width/2, REG_INTENSITY,  width,
               color=HSBC_RED, alpha=0.85, label="监管报送强度指数")
bars2 = ax.bar(x + width/2, BIZ_COMPLEXITY, width,
               color=HSBC_BLUE, alpha=0.85, label="业务复杂度指数")

# Data localisation tier markers
tier_markers = {100: ("▲", HSBC_RED), 60: ("◆", "#FF8C00"), 0: ("●", HSBC_GREEN)}
for i, tier in enumerate(DATA_LOCAL_TIER):
    symbol, color = tier_markers[tier]
    y_pos = max(REG_INTENSITY[i], BIZ_COMPLEXITY[i]) + 2.5
    ax.text(i, y_pos, symbol, ha="center", fontsize=13, color=color, fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(MARKETS, fontsize=9.5, rotation=35, ha="right")
ax.set_ylabel("指数 (0-100)", fontsize=11, color=HSBC_GREY)
ax.set_title("汇丰亚太区: 监管报送强度 vs 业务复杂度 vs 数据本地化约束", fontsize=15,
             fontweight="bold", color=HSBC_RED, pad=16)

# Dual legend
bar_legend = ax.legend(loc="upper left", fontsize=10, frameon=False)
legend_markers = [
    Line2D([0], [0], marker='^', color='w', markerfacecolor=HSBC_RED,  markersize=11,
           label='▲ 强强制本地存储 (9市场)'),
    Line2D([0], [0], marker='D', color='w', markerfacecolor='#FF8C00', markersize=10,
           label='◆ 有条件本地副本 (4市场)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=HSBC_GREEN, markersize=10,
           label='● 自由流转 (2市场: 港/新)'),
]
marker_legend = ax.legend(handles=legend_markers, fontsize=9, loc="upper right", frameon=False)
ax.add_artist(bar_legend)

ax.set_ylim(0, 112)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color(HSBC_GREY)
ax.spines["bottom"].set_color(HSBC_GREY)
ax.tick_params(colors=HSBC_GREY, which="both")
ax.grid(True, alpha=0.15, linestyle="--", axis="y")
save(fig, "chart3_reg_intensity.png")

print("\n✅ All charts generated in:", IMG_DIR)
