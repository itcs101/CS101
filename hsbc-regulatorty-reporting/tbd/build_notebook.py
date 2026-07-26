#!/usr/bin/env python3
"""Build the HSBC APAC Regulatory Reporting Consulting Report as a Jupyter notebook.

Generates an .ipynb with:
  - Mermaid diagrams (sections 2.2, 2.3, 5.2, 5.4, 5.5, 6.2, 7.2)
  - Python matplotlib charts (section 2.4)
  - Markdown tables (sections 3.1, 3.3, 4.1, 7.6, Appendix C)
  - Rich markdown prose throughout
"""

import json, os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "HSBC-APAC-Regulatory-Reporting-Consulting-Report.ipynb")

nb = {"cells": [], "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python",
         "name": "python3"}, "language_info": {"name": "python", "version": "3.10.0"}},
      "nbformat": 4, "nbformat_minor": 5}

def md(source):
    nb["cells"].append({"cell_type": "markdown", "metadata": {}, "source": source if isinstance(source, list) else [source]})

def code(source):
    nb["cells"].append({"cell_type": "code", "metadata": {}, "source": source if isinstance(source, list) else [source],
                         "outputs": [], "execution_count": None})

# ── helpers ──────────────────────────────────────────────────
def mermaid(diagram: str, caption: str = ""):
    """Insert a Mermaid diagram inside a markdown cell."""
    cap = f"\n> *{caption}*\n" if caption else ""
    md(f"```mermaid\n{diagram.strip()}\n```{cap}")

def tbl(headers: list, rows: list[list], caption: str = ""):
    """Insert a markdown table."""
    lines = ["| " + " | ".join(str(h) for h in headers) + " |",
             "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(str(c) for c in r) + " |")
    if caption:
        lines.append(f"\n> *{caption}*")
    md("\n".join(lines))

def h1(title): md(f"# {title}")
def h2(title): md(f"## {title}")
def h3(title): md(f"### {title}")
def h4(title): md(f"#### {title}")
def para(text): md(text)

# ══════════════════════════════════════════════════════════════
# TITLE PAGE
# ══════════════════════════════════════════════════════════════
h1("汇丰集团亚太区监管报送体系优化——致亚太区COO、CDO/CIO 咨询报告")
para("**报告编号：** HSBC-APAC-RR-2026-001 &nbsp;|&nbsp; **版本：** V1.0 &nbsp;|&nbsp; **日期：** 2026-07-25  \n"
     "**密级：** 高度机密——仅限汇丰集团亚太区COO、CDO/CIO及各市场COO、CDO、CIO  \n"
     "**编制：** 亚太区监管报送专家顾问组")

# ══════════════════════════════════════════════════════════════
# 1. EXECUTIVE SUMMARY
# ══════════════════════════════════════════════════════════════
h1("1. 执行摘要")
h2("1.1 报告背景与目的")
para("作为全球系统重要性银行（G-SIBs），汇丰集团亚太区业务覆盖 **22个以上国家和地区**，"
     "涉及**普通法系、大陆法系、伊斯兰法系**三大法律体系，是全球监管报送环境最复杂、报送标准最分散的跨国金融机构。"
     "本报告基于对汇丰亚太区所有运营市场的全面梳理，整合监管要求分类、数据架构、加密技术、伊斯兰金融等多维度分析，"
     "面向亚太区及市场级COO、CDO/CIO，提供监管报送体系优化的战略级咨询建议。")

h2("1.2 核心发现")
para("**六大核心发现：**\n\n"
     "1. **市场覆盖广度导致复杂度指数级放大**：22个亚太市场，各属地监管规则独立、报送标准差异显著，不存在区域级统一协调机制。\n\n"
     "2. **亚太分化为三大法系监管集群**：英美普通法系（港/新/澳/新西）、大陆法系（日/韩/台——亚太合规最高压地带）、混合法系（东南亚+南亚）。\n\n"
     "3. **数据本地化已成全亚太刚性约束**：14个主要市场中，**9个市场实施强制数据本地存储**，原始交易明细禁止离境。\n\n"
     "4. **汇丰现有架构存在五大核心短板**：集团标准与属地规则适配性不足、跨系统数据治理薄弱、自动化覆盖率仅约60%、合规溯源能力不完整、东北亚为最薄弱盲区。\n\n"
     "5. **监管处罚力度显著升级**：2025年香港罚款420万港元，**2026年澳大利亚罚款3500万澳元**——处罚已从警告升级为高额罚款+高管追责。\n\n"
     "6. **伊斯兰金融报送形成独立双轨制**：马来西亚（FSA+IFSA双法案）、中东市场（AAOIFI标准），需独立维护两套报送体系。")

h2("1.3 战略建议概要")
tbl(["战略支柱", "核心举措", "预期价值"],
    [["**区域统筹**", "建立\"集团-区域-属地\"三级协同治理，强化区域总部跨属地合规统筹权", "解决\"集团标准vs属地规则\"根矛盾"],
     ["**数据驱动**", "统一亚太区主数据标准，搭建区域级统一数据中枢（港+新双活）", "从根本上提升报送数据质量"],
     ["**全链路自动化**", "将整体自动化率从~60%提升至90%+，补齐全链路溯源能力", "大幅降低合规运营成本与人为差错"],
     ["**双法系适配**", "搭建英美法系+大陆法系双轨规则引擎，日韩台专项改造", "解决东北亚合规盲区"]])

# ══════════════════════════════════════════════════════════════
# 2. MARKET COVERAGE
# ══════════════════════════════════════════════════════════════
h1("2. 汇丰亚太区市场覆盖与业务全景")
h2("2.1 全亚太市场清单（22个市场无遗漏）")
para("汇丰亚太区管控主体统一为**香港上海汇丰银行有限公司**，所有属地分行、本地法人子银行全部纳入区域矩阵管控。")

tbl(["序号", "市场", "ISO", "经营主体类型", "核心业务属性", "监管体系"],
    [["1", "**中国香港**", "HK", "区域总部法人银行", "全业务枢纽+全球贸易融资中心", "HKMA+SFC"],
     ["2", "**中国大陆**", "CN", "本地法人子行", "外资全牌照银行（规模最大外资行之一）", "NFRA+PBOC+SAFE"],
     ["3", "**中国台湾**", "TW", "本地法人子行", "零售+对公全业务，两岸金融核心", "金管会+中央银行"],
     ["4", "**中国澳门**", "MO", "境外分行", "零售+跨境业务", "AMCM"],
     ["5", "**新加坡**", "SG", "本地法人子行", "东盟跨境枢纽+全球交易银行离岸中心", "MAS"],
     ["6", "**马来西亚**", "MY", "本地法人子行+伊斯兰子行", "全业务+伊斯兰金融双轨制", "BNM"],
     ["7", "**印度尼西亚**", "ID", "本地法人子行", "大宗商品贸易融资+跨境业务", "BI+OJK"],
     ["8", "**泰国**", "TH", "境外分行", "企业批发为主，无大规模零售", "BOT"],
     ["9", "**越南**", "VN", "本地法人子行", "外资制造业供应链+贸易融资", "SBV"],
     ["10", "**菲律宾**", "PH", "境外分行", "跨境贸易+高端个人", "BSP"],
     ["11", "**印度**", "IN", "本地法人子行", "全牌照业务", "RBI"],
     ["12", "**日本**", "JP", "境外分行(东京+大阪)", "纯机构投行批发，无零售", "FSA+BOJ"],
     ["13", "**韩国**", "KR", "境外分行(首尔)", "财阀跨境批发，轻零售", "FSS+BOK"],
     ["14", "**澳大利亚**", "AU", "本地法人子行", "澳新机构业务核心", "APRA+AUSTRAC"],
     ["15", "**新西兰**", "NZ", "本地法人子行", "零售+本地对公", "RBNZ+FMA"],
     ["16", "**孟加拉**", "BD", "境外分行", "贸易融资为主", "BB"],
     ["17", "**斯里兰卡**", "LK", "境外分行", "—", "CBSL"],
     ["18", "**马尔代夫**", "MV", "境外分行", "—", "MMA"],
     ["19", "**毛里求斯**", "MU", "境外分行", "跨境金融服务", "BOM"],
     ["20", "**文莱**", "BN", "境外分行", "—", "BDCB"]],
    "依据：汇丰集团官方Simplified Structure Chart、2025年报、各属地机构官网公开披露文件")

# ── 2.2 MERMAID: Org Structure ──
h2("2.2 汇丰亚太区核心经营主体架构图")
mermaid(r"""
graph TB
    ROOT["<b>香港上海汇丰银行有限公司<br/>The Hongkong & Shanghai Banking Corp. Ltd.</b><br/><i>【亚太区区域控股主体 / 管理总部】</i>"]

    ROOT --> GC["<b>大中华区</b>"]
    ROOT --> ASEAN["<b>东盟 + 南亚</b>"]
    ROOT --> NEA["<b>东北亚 + 大洋洲</b>"]

    GC --> HK["<b>🇭🇰 香港</b><br/>区域总部法人<br/>零售客户700万+"]
    GC --> CN["<b>🇨🇳 中国大陆</b><br/>本地法人子行<br/>外资规模最大"]
    GC --> TW["<b>🇹🇼 台湾</b><br/>本地法人子行<br/>全牌照 两岸核心"]
    GC --> MO["<b>🇲🇴 澳门</b><br/>境外分行"]

    ASEAN --> SG["<b>🇸🇬 新加坡</b><br/>本地法人<br/>东盟跨境枢纽"]
    ASEAN --> MY["<b>🇲🇾 马来西亚</b><br/>法人 + 伊斯兰子行<br/>双轨制"]
    ASEAN --> ID["<b>🇮🇩 印尼</b><br/>本地法人<br/>大宗商品融资"]
    ASEAN --> SEA_OTHER["<b>泰 / 越 / 菲 / 印</b><br/>分行或法人<br/>贸易融资为主"]
    ASEAN --> SA["<b>孟 / 斯 / 马 / 文 / 毛</b><br/>境外分行"]

    NEA --> JP["<b>🇯🇵 日本</b><br/>境外分行 (东京+大阪)<br/>纯机构批发"]
    NEA --> KR["<b>🇰🇷 韩国</b><br/>境外分行 (首尔)<br/>财阀跨境"]
    NEA --> AU["<b>🇦🇺 澳大利亚</b><br/>本地法人<br/>澳新机构核心"]
    NEA --> NZ["<b>🇳🇿 新西兰</b><br/>本地法人<br/>零售+本地对公"]

    style ROOT fill:#DB0011,color:#fff,stroke:#333
    style GC fill:#FFB6C1,stroke:#333
    style ASEAN fill:#FFB6C1,stroke:#333
    style NEA fill:#FFB6C1,stroke:#333
    style HK fill:#E8F5E9,stroke:#333
    style CN fill:#E8F5E9,stroke:#333
    style TW fill:#E8F5E9,stroke:#333
    style MO fill:#E8F5E9,stroke:#333
    style SG fill:#E3F2FD,stroke:#333
    style MY fill:#E3F2FD,stroke:#333
    style ID fill:#E3F2FD,stroke:#333
    style SEA_OTHER fill:#E3F2FD,stroke:#333
    style SA fill:#E3F2FD,stroke:#333
    style JP fill:#FFF3E0,stroke:#333
    style KR fill:#FFF3E0,stroke:#333
    style AU fill:#FFF3E0,stroke:#333
    style NZ fill:#FFF3E0,stroke:#333
""", "汇丰亚太区经营主体架构（关键差异: 日韩为分行制，台/新/澳/纽/中/马为本地法人制）")

# ── 2.3 MERMAID: Customer-Product Matrix ──
h2("2.3 汇丰亚太区客群分层与产品矩阵")
mermaid(r"""
graph LR
    subgraph CUST["客群分层 (四大核心层级)"]
        direction TB
        C1["<b>超高净值个人 / 家族办公室</b><br/>Triple I 专属平台<br/>合规复杂度: ★★★★"]
        C2["<b>高净值富裕个人</b><br/>Premier / Premier Elite / Jade<br/>合规复杂度: ★★★"]
        C3["<b>头部企业 / 金融机构</b><br/>亚洲第一交易银行<br/>合规复杂度: ★★★★★"]
        C4["<b>创新型 / 中型企业</b><br/>高增长潜力<br/>合规复杂度: ★★"]
    end

    subgraph PROD["核心产品四大板块"]
        direction TB
        P1["<b>财富管理</b><br/>多币种储蓄/信贷/投资/保险<br/>卓越理财·尊尚国际通"]
        P2["<b>跨境贸易与外汇</b><br/>贸易融资/现金管理/外汇套保<br/>区域内极速汇"]
        P3["<b>资本市场与证券</b><br/>债务/股权融资/多币种财资<br/>证券托管"]
        P4["<b>伊斯兰金融 (特色)</b><br/>Murabaha/Sukuk/Takaful<br/>马来西亚+中东"]
    end

    subgraph COVER["主要覆盖市场"]
        direction TB
        M1["港 新 中 台 澳"]
        M2["全部市场"]
        M3["港 新 日 澳 印"]
        M4["马来西亚 中东关联"]
    end

    C1 --> P1
    C2 --> P1
    C3 --> P2
    C3 --> P3
    C4 --> P2
    P1 --> M1
    P2 --> M2
    P3 --> M3
    P4 --> M4

    style CUST fill:#f5f5f5,stroke:#DB0011
    style PROD fill:#f5f5f5,stroke:#DB0011
    style COVER fill:#f5f5f5,stroke:#DB0011
    style C3 fill:#FFD700,stroke:#333
""", "战略核心: \"高价值、强跨境、易合规\"——主动收缩非核心零售（菲/澳已执行）")

# ── 2.4 PYTHON CHARTS ──
h2("2.4 汇丰亚太区各市场业务规模与结构概览")
para("基于汇丰2025年年报、各市场官网及行业报告(Dataintelo, PW Consulting)公开数据整理。以下通过 Python 图表展示各市场相对业务规模对比。")

code(r'''import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── HSBC brand colours ──
HSBC_RED   = "#DB0011"
HSBC_GREY  = "#666666"
HSBC_LIGHT = "#F5F5F5"
PALETTE     = ["#DB0011", "#C0003C", "#A0004B", "#800050", "#600050",
               "#4B0082", "#2E5090", "#1E90FF", "#00A86B", "#50C878",
               "#FFD700", "#FF8C00", "#FF6347", "#8B4513"]

# ── Data (estimated from public sources) ──
markets = ["香港", "中国大陆", "台湾", "新加坡", "马来西亚", "澳大利亚",
           "印度", "印尼", "日本", "韩国", "泰国", "越南", "菲律宾", "新西兰"]
retail    = [35, 15, 30, 20, 25, 35, 20, 10,  0, 10,  0, 30, 40, 55]
corporate = [40, 50, 40, 45, 45, 40, 50, 60, 80, 90, 80, 70, 60, 25]
wealth    = [25, 35, 30, 35, 20, 25, 30, 30, 20,  0, 20,  0,  0, 20]
islamic   = [ 0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0]

y = np.arange(len(markets))

# ── Chart 1: Stacked horizontal bar – business mix ──
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

b1 = ax.barh(y, retail,    color="#DB0011", label="零售银行")
b2 = ax.barh(y, corporate, left=retail, color="#2E5090", label="对公/企业银行")
left2 = [r + c for r, c in zip(retail, corporate)]
b3 = ax.barh(y, wealth, left=left2, color="#FFD700", label="财富管理")
left3 = [l + w for l, w in zip(left2, wealth)]
b4 = ax.barh(y, islamic, left=left3, color="#00A86B", label="伊斯兰金融")

ax.set_yticks(y)
ax.set_yticklabels(markets, fontsize=10)
ax.set_xlabel("业务占比 (%)", fontsize=11, color=HSBC_GREY)
ax.set_title("汇丰亚太区主要市场业务结构对比 (基于公开数据估计)", fontsize=14, fontweight="bold", color=HSBC_RED, pad=15)
ax.legend(loc="lower right", fontsize=9, ncol=4)
ax.set_xlim(0, 115)
ax.invert_yaxis()

# annotate total
for i, (r, c, w, isl) in enumerate(zip(retail, corporate, wealth, islamic)):
    ax.text(r + c + w + isl + 1, i, f"{r+c+w+isl}%", va="center", fontsize=8, color=HSBC_GREY)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("/tmp/hsbc_business_mix.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print("✅ Chart 1 saved: business mix by market")

# ── Chart 2: Market relative size (bubble) ──
fig2, ax2 = plt.subplots(figsize=(14, 7))
fig2.patch.set_facecolor("white")
ax2.set_facecolor("white")

relative_size = [100, 45, 18, 35, 22, 20, 16, 12, 8, 7, 6, 8, 6, 10]
automation    = [92, 75, 45, 88, 55, 78, 50, 40, 35, 30, 42, 38, 45, 50]
colors_map    = [HSBC_RED if s > 30 else "#2E5090" if s > 12 else HSBC_GREY for s in relative_size]

scatter = ax2.scatter(relative_size, automation, s=[s * 8 for s in relative_size],
                      c=colors_map, alpha=0.8, edgecolors="white", linewidth=1)
for i, mkt in enumerate(markets):
    offset = 1.5 if i % 2 == 0 else -2.5
    ax2.annotate(mkt, (relative_size[i], automation[i]),
                 textcoords="offset points", xytext=(0, offset), fontsize=8,
                 ha="center", color=HSBC_GREY)

ax2.set_xlabel("相对业务规模 (香港=100)", fontsize=11, color=HSBC_GREY)
ax2.set_ylabel("报送自动化率 (%)", fontsize=11, color=HSBC_GREY)
ax2.set_title("汇丰亚太区各市场：业务规模 vs 报送自动化率", fontsize=14,
              fontweight="bold", color=HSBC_RED, pad=15)
ax2.axhline(y=60, color=HSBC_RED, linestyle="--", alpha=0.5, label="当前全区域平均自动化率 (~60%)")
ax2.axhline(y=90, color="#00A86B", linestyle="--", alpha=0.5, label="目标自动化率 (90%+)")
ax2.legend(fontsize=9)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(True, alpha=0.2, linestyle="--")
plt.tight_layout()
plt.savefig("/tmp/hsbc_bubble.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print("✅ Chart 2 saved: business size vs automation rate")
''')

para("**数据口径说明**：以上数据为基于汇丰公开年报、各市场官网业务描述及行业报告的汇总估计，用于呈现相对规模对比。具体精确业务数据请参考汇丰年报各市场章节。")

# ── 2.4b: Regulation intensity by market ──
h2("2.5 亚太区监管强度与业务复杂度综合视图")
code(r'''fig3, ax3 = plt.subplots(figsize=(14, 8))
fig3.patch.set_facecolor("white")
ax3.set_facecolor("white")

markets_arr = np.array(markets)
reg_intensity   = [95, 90, 88, 88, 78, 82, 70, 72, 92, 95, 65, 68, 60, 75]   # 监管强度
biz_complexity  = [95, 82, 75, 85, 80, 70, 65, 60, 55, 62, 50, 52, 48, 58]   # 业务复杂度
data_local      = [0, 100, 100, 100, 100, 60, 60, 100, 60, 100, 60, 100, 60, 100]  # 0=自由, 60=副本, 100=强强制

x = np.arange(len(markets_arr))
width = 0.35

bars1 = ax3.bar(x - width/2, reg_intensity, width, label="监管报送强度指数", color=HSBC_RED, alpha=0.85)
bars2 = ax3.bar(x + width/2, biz_complexity, width, label="业务复杂度指数", color="#2E5090", alpha=0.85)

# Mark data localisation tier
for i, dl in enumerate(data_local):
    marker = "🔒" if dl == 100 else "🔐" if dl == 60 else "🌐"
    ax3.text(i, max(reg_intensity[i], biz_complexity[i]) + 2, marker, ha="center", fontsize=12)

ax3.set_xticks(x)
ax3.set_xticklabels(markets_arr, fontsize=9)
ax3.set_ylabel("指数 (0-100)", fontsize=11, color=HSBC_GREY)
ax3.set_title("汇丰亚太区：监管报送强度 vs 业务复杂度 vs 数据本地化约束", fontsize=14,
              fontweight="bold", color=HSBC_RED, pad=15)
ax3.legend(fontsize=10, loc="upper right")
ax3.set_ylim(0, 115)
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# legend for markers
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], marker='o', color='w', markerfacecolor=HSBC_RED, markersize=12, label='🔒 强强制本地存储'),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFD700', markersize=12, label='🔐 有条件本地副本'),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='#00A86B', markersize=12, label='🌐 自由流转')]
ax3.legend(handles=custom_lines, fontsize=9, loc="lower right")
plt.tight_layout()
plt.savefig("/tmp/hsbc_reg_intensity.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.show()
print("✅ Chart 3 saved: regulation intensity vs business complexity")
''')

# ══════════════════════════════════════════════════════════════
# 3. REGULATORY TAXONOMY
# ══════════════════════════════════════════════════════════════
h1("3. 亚太区监管要求五级分类汇总")

h2("3.1 统一五级分类标准框架")
para("基于对亚太区14个核心市场（中/港/台/日/韩/新/澳/新西/马/印尼/泰/越/菲/印）监管报表的全面梳理，"
     "建立以下**五级统一分类标准**，用于集团报送平台分层架构。")

tbl(["Level", "层级名称", "涵盖范围", "示例"],
    [["**L1**", "**一级大类 (5类)**", "全区域统一、集团报送平台分层顶层",
      "审慎资本流动性 / 交易级明细监管 / 跨境外汇收支 / AML·CFT税务 / 本地特色专项"],
     ["**L2**", "**二级子类 (25类)**", "每一大类下固定拆分、集团统一字段映射基准",
      "资本充足RWA / 流动性LCR·NSFR / 大额风险暴露 / 对公信贷全量明细 / BOP国际收支 / CTR大额现金 / ..."],
     ["**L3**", "**监管机构体系**", "属地监管机构 → 系统路由 & 权限控制",
      "HKMA(港) / NFRA·PBOC(中) / 金管会(台) / FSA(日) / FSS(韩) / MAS(新) / APRA(澳) / RBNZ(新西) / BNM(马) / OJK·BI(印尼) / BOT(泰) / SBV(越) / BSP(菲) / RBI(印)"],
     ["**L4**", "**报表官方编号/模板名**", "监管机构发布的正式报表标识",
      "G01/G11/G40 (中国1104) / MA(BS)系列 (港) / MAS600系列 (新) / APS/S系列 (澳) / B系列 (台) / S10/S21/S50 (新西)"],
     ["**L5**", "**报送频率**", "调度引擎时间窗口控制",
      "日 / 周 / 月 / 季 / 半年 / 年 / 实时触发"]])

h2("3.2 全亚太14个核心市场——监管要求逐市场详细分类汇总")
para("以下按大中华区、东北亚、东南亚、南亚、大洋洲四大区域板块，逐市场列出核心监管报表与关键合规约束。")

# ── Market details as collapsible markdown ──
for region_name, markets_data in [
    ("大中华区 (4市场)", [
        ("A. 中国香港 (HKMA+SFC)", [
            ["1.审慎资本流动性", "MA(BS)系列月报、KM1核心指标、CC1资本构成、LR杠杆率、LCR/NSFR模板、Pillar3半年度披露、LAC吸收亏损能力专项", "Basel III Final Reform完全落地；**LAC规则为香港独有**"],
            ["2.交易级明细", "信贷资产逐笔明细、衍生品交易明细", "GDR 3.0推进中——\"一次报送、多次使用\""],
            ["3.跨境外汇收支", "离岸人民币跨境业务统计、外币敞口月报、跨境同业往来(MA(BS)9)", "离岸人民币中心特殊监管"],
            ["4.AML/税务", "CTR大额现金、STR可疑交易、CRS税务、FATCA美国税务", "FATCA+CRS双轨"],
            ["5.本地特色", "**证券投行关联披露**、存款保险、港元货币发行储备", "2025年罚款420万港元案例"],
        ]),
        ("B. 中国大陆 (NFRA+PBOC+SAFE)", [
            ["1.审慎资本流动性", "1104体系：G01/G03/G40/G21/G11/G14/S63", "《商业银行资本管理办法》季度报送"],
            ["2.交易级明细", "**EAST全量明细**：对公信贷、零售房贷、同业、理财、股权穿透", "监管现场检查核心抓手"],
            ["3.跨境外汇收支", "BOP国际收支(T+1)、外债统计、跨境人民币、ODI对外直接投资", "SAFE严格外汇管控"],
            ["4.AML/税务", "大额/可疑交易报告、CRS境外税务居民信息", "现金交易强管控"],
            ["5.本地特色", "房地产贷款专项、普惠金融专项、地方政府融资平台专项", "三大结构性监管重点"],
            ["🚫 数据约束", "**所有客户交易数据境内本地存储，不得擅自出境**", "《网络安全法》《个人信息保护法》"],
        ]),
        ("C. 中国台湾 (金管会+中央银行)", [
            ["1.审慎资本流动性", "B系列资本充足月报、流动性期限缺口表、不良贷款季报", "本地法人独立报送"],
            ["2.交易级明细", "**全账户交易级明细日报**、对公授信穿透、个人信托资产明细", "频次高、字段密"],
            ["3.跨境外汇收支", "**两岸金融业务专项报表（亚太独有）**、外汇收支逐笔申报", "两岸穿透强监管"],
            ["4.AML/税务", "CTR大额、STR可疑、CRS税务居民", "—"],
            ["5.本地特色", "两岸资金往来专项统计、不动产房贷专项、证券信托代销专项", "全亚太独有两岸规则"],
            ["🚫 数据约束", "**两岸业务专项报送原始台账禁止出境存储**", "金管会金融资讯安全规范"],
        ]),
    ]),
    ("东北亚 (2市场——亚太合规最高压地带)", [
        ("E. 日本 (FSA+BOJ)", [
            ["1.审慎资本流动性", "月度资本充足简表、外币流动性头寸季报、大额风险暴露台账", "分行制无需独立法人资本"],
            ["2.交易级明细", "**衍生品逐笔交易明细、同业拆借全量台账**", "⚠️ 交易级明细100%留存，监管可任意周期回溯核查"],
            ["3.跨境外汇收支", "外汇交易日报、跨境投融资季度明细、对外债权债务统计", "日元跨境资本流动强监控"],
            ["4.AML/税务", "CTR大额、IFT跨境、STR可疑、CRS税务", "—"],
            ["5.本地特色", "日元衍生品风险敞口专项、对日外资企业跨境资金台账", "—"],
        ]),
        ("F. 韩国 (FSS+BOK)", [
            ["1.审慎资本流动性", "分行资本风险简表、外币流动性月度压力测试", "分行制"],
            ["2.交易级明细", "**财阀集团关联授信穿透明细表**、外汇衍生品逐笔明细", "财阀关联交易为报送高风险点"],
            ["3.跨境外汇收支", "跨境资本流动**实时报送**、对外投资季报、集团资金池归集明细", "⚠️ 外汇报送零容错+高管追责双罚制"],
            ["4.AML/税务", "CTR大额、跨境IFT、STR可疑、CRS税务", "—"],
            ["5.本地特色", "**大型财阀关联交易专项**、半导体供应链跨境资金统计", "韩国独有财阀监管"],
            ["🚫 数据约束", "**韩元外汇交易、财阀关联交易原始数据必须本地留存**", "个人信息保护法、FSS安全指引"],
        ]),
    ]),
    ("东南亚+东盟 (6市场)", [
        ("G. 新加坡 (MAS)", [
            ["1.审慎资本流动性", "**MAS600系列**：资本充足、流动性、杠杆率月报；Pillar3；大额风险暴露", "Notice 637/651"],
            ["2.交易级明细", "信贷、衍生品、资管全量交易明细", "**所有跨境交易溯源数据本地留存>5年**"],
            ["3.跨境外汇收支", "东盟跨境资金池统计、多币种外汇头寸月报", "东盟跨境枢纽"],
            ["4.AML/税务", "CTR/IFT/STR、CRS/FATCA", "MAS Compliance Toolkit"],
            ["5.本地特色", "伊斯兰金融专项、东盟跨境财资管理专项、存款保险", "双金融体系"],
        ]),
        ("H. 马来西亚 (BNM)——双轨制核心", [
            ["1.审慎资本流动性", "BNM资本充足季报、流动性缺口表、不良贷款质量报表", "传统银行+伊斯兰银行双套"],
            ["2.交易级明细", "对公/零售信贷全量明细、**伊斯兰教法合规交易明细**", "双轨制明细"],
            ["3.跨境外汇收支", "跨境贸易融资专项、外币头寸月报", "马币外汇管制"],
            ["4.AML/税务", "CTR/STR、CRS税务报送", "**DCR数据合规报告(自2020年)**"],
            ["5.本地特色", "**IFSA伊斯兰金融全套专项报表**、Shariah不合规事件报告、棕榈油贷款统计", "FSA+IFSA双法案"],
        ]),
        ("I. 印度尼西亚 (BI+OJK)", [
            ["1.审慎资本流动性", "OJK月度资本/流动性/资产质量报表", "半年期核心审慎"],
            ["2.交易级明细", "大宗商品贸易融资逐笔明细、对公授信穿透", "大宗商品(棕榈/矿产)专项"],
            ["3.跨境外汇收支", "进出口外汇收支**逐笔申报**、外债统计", "印尼盾严格外汇管制"],
            ["🚫 数据约束", "**全部交易数据境内本地存储，严格禁止出境**", "GR71电子交易条例"],
        ]),
        ("J. 泰国 (BOT)", [
            ["1.审慎资本流动性", "分行资本与外币流动性季度简表、大额风险暴露台账", "境外分行制"],
            ["2.交易级明细", "进出口贸易融资逐笔明细、外资企业授信明细", ">200万泰铢现金强制实时CTR"],
            ["3.跨境外汇收支", "跨境外汇收支月报、境外投资季度统计", "泰铢跨境流动管控"],
        ]),
        ("K. 越南 (SBV)", [
            ["1.审慎资本流动性", "SBV月度资本充足/流动性/资产质量报表", "半年期核心审慎"],
            ["2.交易级明细", "外资制造企业授信明细、房地产贷款逐笔台账", "外资供应链专项"],
            ["🚫 数据约束", "**所有本地用户金融数据境内存储，出境需公安部专项审批**", "《越南网络安全法》第26条"],
        ]),
        ("L. 菲律宾 (BSP)", [
            ["1.审慎资本流动性", "分行外币流动性月度、大额风险暴露台账", "季度核心审慎"],
            ["2.交易级明细", "进出口贸易融资逐笔明细、外资企业授信明细", "**海外劳工侨汇专项（菲律宾独有）**"],
            ["3.跨境外汇收支", "**海外侨汇专项统计表**、跨境外汇收支月报", "侨汇为GDP重要支柱"],
        ]),
    ]),
    ("南亚 (1核心市场) + 大洋洲 (2市场)", [
        ("M. 印度 (RBI)", [
            ["1.审慎资本流动性", "RBI月度资本充足/流动性/不良贷款资产质量", "独立审慎框架"],
            ["2.交易级明细", "对公授信穿透、零售信贷全量明细", "中小企业/农业信贷强制统计"],
            ["3.跨境外汇收支", "FDI外商投资季报、进出口外汇收支逐笔申报、外债统计", "卢比严格外汇管制"],
            ["🚫 数据约束", "**支付类数据100%境内存储，无监管许可不得出境**", "RBI支付数据本地化强制通知"],
        ]),
        ("N. 澳大利亚 (APRA+AUSTRAC)", [
            ["1.审慎资本流动性", "APRA APS资本/流动性季报、S系列、S50贷款月报、Pillar3", "CPS 234信息安全"],
            ["2.交易级明细", "个人房贷逐笔明细、对公授信穿透、证券托管交易明细", "消费者数据隐私强保护"],
            ["3.跨境外汇收支", "**跨境IFT国际划转逐笔报送（全量强制）**", "AUSTRAC独有强度"],
            ["4.AML/税务", "TTR大额现金、**SMR可疑交易**、年度AML合规报告", "AUSTRAC独立强监管"],
            ["⚠️ 处罚", "2026年反诈报送缺陷罚款**3500万澳元**", "近年亚太区最大单笔合规处罚"],
        ]),
        ("O. 新西兰 (RBNZ+FMA)", [
            ["1.审慎资本流动性", "RBNZ S10/S21/S50、季度资本充足与流动性", "**本地法人资本隔离**"],
            ["🚫 数据约束", "**本地法人底层业务数据物理隔离，禁止境外集中存储原始明细**", "RBNZ审慎信息安全规则"],
        ]),
    ]),
]:
    h4(region_name)
    for mkt_name, rows in markets_data:
        h4(mkt_name)
        tbl(["分类", "核心报表/规范", "关键合规约束"], rows)

# ── 3.3 HEATMAP TABLE ──
h2("3.3 全区域共性监管要求热力图")
para("● = 有明确监管要求 &nbsp;&nbsp; ◐ = 部分覆盖/有限要求 &nbsp;&nbsp; ○ = 无强制/自由流转")

tbl(["市场", "审慎资本流动性", "交易明细颗粒报送", "跨境外汇收支", "AML/CFT税务", "本地特色专项", "数据本地存储强制程度"],
    [["中国香港",     "●", "●", "●", "●", "●", "○ (自由)"],
     ["中国大陆",     "●", "●", "●", "●", "●", "● (强强制)"],
     ["中国台湾",     "●", "●", "●", "●", "●", "● (强强制)"],
     ["日本",         "●", "●", "●", "●", "○", "◐ (副本)"],
     ["韩国",         "●", "●", "●", "●", "●", "● (强强制)"],
     ["新加坡",       "●", "●", "●", "●", "●", "○ (自由)"],
     ["马来西亚",     "●", "●", "●", "●", "●", "● (强强制)"],
     ["印度尼西亚",   "●", "●", "●", "●", "○", "● (强强制)"],
     ["泰国",         "●", "◐", "●", "●", "○", "◐ (副本)"],
     ["越南",         "●", "●", "●", "●", "○", "● (强强制)"],
     ["菲律宾",       "●", "◐", "●", "●", "●", "◐ (副本)"],
     ["印度",         "●", "●", "●", "●", "●", "● (强强制)"],
     ["澳大利亚",     "●", "●", "●", "●", "●", "◐ (副本)"],
     ["新西兰",       "●", "●", "●", "●", "○", "● (强强制)"]],
    "全亚太14核心市场共性监管要求覆盖热力图")

h3("五大共性监管结论")
para("1. **100%市场覆盖审慎资本流动性+AML/CFT+跨境外汇收支**——集团标准化改造核心优先项\n\n"
     "2. **发达经济体全面推行交易级细粒度明细报送**，东南亚正快速跟进\n\n"
     "3. **9/14市场（64%）实施数据本地存储强制约束**——原始交易数据无法统一归集区域中枢\n\n"
     "4. **AML报表全区域规则趋同**（CTR/STR/IFT/CRS）——可搭建集团统一AML模块\n\n"
     "5. **属地差异核心集中在第五类（本地特色专项）**——最大定制化开发成本来源")

# ══════════════════════════════════════════════════════════════
# 3.4 ISLAMIC FINANCE SECTION
# ══════════════════════════════════════════════════════════════
h2("3.4 伊斯兰金融双轨制监管专项说明")
para("马来西亚为汇丰亚太区**唯一**运营伊斯兰子银行（HSBC Amanah Malaysia Berhad）的市场。"
     "中东关联市场（沙特SABB、阿联酋等）通过关联实体运营。")

tbl(["维度", "传统银行", "伊斯兰银行", "汇丰涉及市场"],
    [["法律框架", "《2013年金融服务法案》(FSA)", "《2013年伊斯兰金融服务法案》(IFSA)", "马来西亚"],
     ["财务报告准则", "MFRS", "MFRS + Shariah合同信息披露 + 股息支付要求", "马来西亚"],
     ["操作风险报告", "ORR系统（LED+KRI+SA）", "ORR系统 + Shariah不合规事件专项报告", "马来西亚"],
     ["会计标准", "IFRS/IAS", "**AAOIFI标准**（伊斯兰金融机构会计与审计组织）", "马来西亚+中东"],
     ["审慎规则", "Basel III标准", "Basel III + 伊斯兰金融附加审慎要求（如SAMA信用/市场风险附加规定）", "马来西亚+中东"],
     ["治理架构", "董事会+审计委员会", "董事会+**独立Shariah委员会**+**Shariah审计官**（任命需监管批准）", "全部伊斯兰金融市场"]])

# ══════════════════════════════════════════════════════════════
# 4. DATA LOCALISATION TABLE
# ══════════════════════════════════════════════════════════════
h1("4. 数据本地存储与跨境约束全景分析")
h2("4.1 三大类别市场分类表")

tbl(["类别", "市场", "法规依据", "强制范围", "跨境限制"],
    [
     ["**第一类：强强制本地存储**<br/>(9市场)", "中国大陆", "《网络安全法》《个人信息保护法》", "全部客户身份资料、信贷/存款/同业/理财交易明细、反洗钱底层数据、EAST原始明细", "原始交易明细、客户敏感数据出境必须走数据出境安全评估"],
     ["", "中国台湾", "金管会金融资讯安全规范、个人资料保护法", "新台币账户交易、两岸跨境资金明细、个人财富/信托全量数据", "**两岸业务专项报送原始台账禁止出境存储**"],
     ["", "韩国", "个人信息保护法、BOK外汇监管数据留存规则", "韩元外汇交易、财阀关联交易、跨境资本流动逐笔台账", "仅聚合指标可跨境"],
     ["", "新西兰", "RBNZ审慎信息安全规则、隐私法", "本地居民房贷、零售存款、小微企业信贷全量明细", "**本地法人底层数据物理隔离，禁止境外集中**"],
     ["", "印度尼西亚", "OJK金融监管条例、GR71电子交易条例", "全部本地客户交易、信贷、外汇、反洗钱明细", "跨境传输需双重审批"],
     ["", "越南", "《越南网络安全法》第26条", "越南盾交易、外资制造企业授信、外债、贸易融资原始明细", "出境需公安部专项审批"],
     ["", "印度", "RBI支付数据本地化强制通知", "卢比支付清算、FDI外商投资底层明细", "支付类数据100%境内存储"],
     ["", "马来西亚", "BNM金融数据安全指引", "马币本地交易、伊斯兰金融专项台账、棕榈油产业信贷明细", "原始明细不得长期境外存放"],
     ["", "日本 (部分强制)", "FSA金融厅信息安全指引", "全量交易台账境内留存完整副本", "允许汇总指标跨境"],
     ["**第二类：本地副本**<br/>(4市场)", "澳大利亚", "APRA CPS 234、AUSTRAC留存规则", "客户信贷、跨境IFT划转、房贷明细", "本地保留完整副本，监管检查优先调取境内存储"],
     ["", "泰国", "BOT数据管理规范", "大额现金CTR、进出口贸易融资台账", "仅统计汇总表可存放境外"],
     ["", "菲律宾", "BSP银行业数据指引", "海外侨汇、跨境贸易原始明细", "本地留存完整副本"],
     ["", "日本 (副本部分)", "BOJ外汇台账留存规则", "衍生品、跨境投融资原始明细", "本地即时可调取"],
     ["**第三类：自由流转**<br/>(2市场)", "中国香港", "HKMA资讯科技风险管理指引", "无数据本地化强制条款", "可作为全亚太汇总数据中心"],
     ["", "新加坡", "MAS科技风险管理指引、PDPA", "不强制金融数据本地存储", "可作为亚太统一报送数据处理双活中枢"],
    ], "数据本地存储三大类别详细对比")

# ══════════════════════════════════════════════════════════════
# 5. DISTRIBUTED DATA PROCESSING ARCHITECTURE
# ══════════════════════════════════════════════════════════════
h1("5. 分布式数据处理架构方案")
h2("5.1 架构设计核心原则")
para("基于**\"本地计算+仅汇总出境\"**的核心设计理念：\n\n"
     "1. **原始数据不出属地**：所有交易级明细在属地本地节点完成计算\n"
     "2. **计算靠近数据**：监管指标运算逻辑全部下沉到属地本地执行\n"
     "3. **仅加密汇总结果跨境**：仅传输不可还原至个体的聚合统计指标\n"
     "4. **双活中枢容灾**：香港+新加坡双活承载全亚太汇总数据，互为灾备")

# ── 5.2 MERMAID: Full Architecture ──
h2("5.2 分布式数据处理整体架构图（五层架构）")
mermaid(r"""
graph TB
    subgraph L5["<b>Layer 5: 全链路溯源审计层</b> — OpenLineage + 不可篡改日志 (留存7-20年)"]
        AUDIT["审计日志仓库<br/>不可篡改存储<br/>一键溯源证明"]
    end

    subgraph L4["<b>Layer 4: 统一加密传输层</b> — TLS 1.3 + AES-256 + 专线VPN"]
        TX["加密传输通道<br/>仅汇总指标/密文指纹"]
    end

    subgraph L3["<b>Layer 3: 属地级规则适配层 (轻量化)</b>"]
        direction LR
        R_CN["中 规则适配"]
        R_HK["港 格式转换"]
        R_TW["台 两岸专项"]
        R_JP["日 衍生品专项"]
        R_KR["韩 财阀专项"]
        R_SG["新 MAS600"]
        R_MY["马 伊斯兰专项"]
    end

    subgraph L2["<b>Layer 2: 区域级统一数据处理中枢层</b> (香港+新加坡 双活GCP)"]
        direction LR
        HUB_HK["<b>🇭🇰 香港中枢</b><br/>统一数据清洗/标准化<br/>字段映射/质量校验<br/>ODS/数据湖"]
        HUB_SG["<b>🇸🇬 新加坡中枢</b><br/>统一数据清洗/标准化<br/>字段映射/质量校验<br/>ODS/数据湖"]
    end

    subgraph L1["<b>Layer 1: 多源统一数据采集层</b> — CDC实时捕获 + 批量导入"]
        direction LR
        subgraph L1A["<b>强本地化市场 (9个)</b><br/>独立部署本地全栈"]
            N_CN["🇨🇳 中<br/>TDE+本地计算+MPC"]
            N_TW["🇹🇼 台<br/>TDE+本地计算+MPC"]
            N_KR["🇰🇷 韩<br/>TDE+本地计算+MPC"]
            N_OTH["🇳🇿🇮🇩🇻🇳🇮🇳🇲🇾"]
        end
        subgraph L1B["<b>本地副本 (4个)</b><br/>完整镜像 + 中枢全量"]
            N_JP["🇯🇵 日"]
            N_AU["🇦🇺 澳"]
            N_TH["🇹🇭 泰"]
            N_PH["🇵🇭 菲"]
        end
        subgraph L1C["<b>自由流转 (2个)</b><br/>直接归集中枢"]
            N_HK["🇭🇰 港"]
            N_SG["🇸🇬 新"]
        end
    end

    L1A & L1B & L1C -->|加密管道 TLS 1.3| HUB_HK
    L1A & L1B & L1C -->|加密管道 TLS 1.3| HUB_SG
    HUB_HK & HUB_SG --> L3
    L3 --> TX
    TX -->|监管报送报文| AUDIT
    HUB_HK <-->|双活同步| HUB_SG

    style L5 fill:#E8F5E9,stroke:#00A86B
    style L4 fill:#FFF3E0,stroke:#FF8C00
    style L3 fill:#E3F2FD,stroke:#2E5090
    style L2 fill:#FFE0E0,stroke:#DB0011
    style L1 fill:#F5F5F5,stroke:#666
""", "汇丰亚太区监管报送分布式数据处理五层架构 (目标态)")

# ── 5.4 MERMAID: AML MPC Flow ──
h2("5.4 反洗钱（AML）跨市场关联筛查——MPC多方安全计算分布式流程")
mermaid(r"""
sequenceDiagram
    participant A as 属地A (如香港)
    participant B as 属地B (如新加坡)
    participant C as 属地C (如中国大陆)
    participant HUB as 区域中枢 (港/新)

    Note over A,B,C: ─── 本地执行阶段 (原始数据全程不出属地) ───

    A->>A: ①加载本地全量交易明细
    A->>A: ②本地规则引擎执行AML筛查<br/>(大额/分拆/跨境/涉敏/快进快出)
    A->>A: ③本地计算: 可疑交易数/风险客户总数<br/>风险等级分布/跨境可疑总额
    A->>A: ④MPC节点生成加密客户指纹(秘密分片)

    B->>B: ①加载本地全量交易明细
    B->>B: ②本地规则引擎执行AML筛查
    B->>B: ③本地计算各项AML指标
    B->>B: ④MPC节点生成加密客户指纹(秘密分片)

    C->>C: ①加载本地全量交易明细
    C->>C: ②本地规则引擎执行AML筛查
    C->>C: ③本地计算各项AML指标
    C->>C: ④MPC节点生成加密客户指纹(秘密分片)

    Note over A,HUB: ─── 跨境传输阶段 (仅加密结果) ───

    A->>HUB: AES-256加密汇总指标 + MPC加密分片
    B->>HUB: AES-256加密汇总指标 + MPC加密分片
    C->>HUB: AES-256加密汇总指标 + MPC加密分片

    Note over HUB: ─── 中枢处理阶段 ───

    HUB->>HUB: ⑤MPC密文比对各属地指纹
    HUB->>HUB: ⑥仅返回: 跨市场关联风险计数<br/>(不返回任何客户明细)
    HUB->>HUB: ⑦聚合全区域AML风险汇总报表

    Note over A,HUB: 原始流水/客户姓名/账户号 全程不出属地
""", "已有落地验证：汇丰大湾区跨境理财通已采用同款MPC架构通过HKMA+人行合规验收")

# ── 5.5 MERMAID: Prudential Reporting Flow ──
h2("5.5 审慎监管报表分布式处理流程")
mermaid(r"""
flowchart LR
    subgraph LOCAL["<b>属地本地节点</b>"]
        direction TB
        S1["① 本地数据源加载<br/>核心银行/信贷/交易/AML"]
        S2["② 本地计算全部<br/>报表行项/指标/校验逻辑"]
        S3["<b>两套输出</b>"]
        S3A["明细报文 → 直报属地监管"]
        S3B["汇总指标 → AES-256加密出境"]
        S1 --> S2 --> S3
        S3 --> S3A
        S3 --> S3B
    end

    subgraph HUB["<b>区域中枢 (港/新)</b>"]
        direction TB
        H1["③ 各属地汇总指标<br/>FHE二次聚合"]
        H2["④ 集团合并审慎报表"]
        H3["→ 集团总部<br/>→ 境外监管<br/>→ 管理层看板"]
        H1 --> H2 --> H3
    end

    S3B -->|加密汇总指标| H1

    style LOCAL fill:#FFF3E0,stroke:#FF8C00
    style HUB fill:#FFE0E0,stroke:#DB0011
    style S3A fill:#E8F5E9,stroke:#00A86B
    style S3B fill:#E3F2FD,stroke:#2E5090
""", "审慎监管报表: 本地完整计算 → 明细直报属地监管 → 汇总加密出境 → 中枢聚合集团报表")

# ══════════════════════════════════════════════════════════════
# 6. TOKENIZATION
# ══════════════════════════════════════════════════════════════
h1("6. 数据 Tokenization 技术方案")
h2("6.1 Tokenization 在监管报送场景中的定位")
para("**Tokenization（令牌化）**是将敏感数据替换为无实际意义的替代标识符的技术。"
     "与加密不同，Token 无法通过数学运算还原——映射关系存储在独立的、高安全级别的**令牌库 (Token Vault)** 中。\n\n"
     "**核心价值**：在满足监管报送功能需求的同时，大幅降低敏感数据在传输和处理过程中的泄露风险。")

# ── 6.2 MERMAID: 4-Layer Tokenization ──
h2("6.2 Tokenization 四层方案架构")
mermaid(r"""
graph TB
    subgraph L1["<b>Layer 1: 格式保持令牌化 (FPT)</b><br/>适用: 监管报表客户标识字段替代 — NIST SP 800-38G FF1算法"]
        direction LR
        FPT_IN["原始: CN-110108-19900101-123X"]
        FPT_ENGINE["<b>FPT引擎</b><br/>FF1算法 + 确定性/随机模式"]
        FPT_VAULT["<b>Token Vault</b><br/>独立安全存储<br/>HSM保护"]
        FPT_OUT["令牌: CN-582913-84072601-456Y<br/>保持格式/校验位有效/无法还原"]
        FPT_IN --> FPT_ENGINE --> FPT_OUT
        FPT_ENGINE <--> FPT_VAULT
    end

    subgraph L2["<b>Layer 2: 确定性令牌化</b><br/>适用: 跨系统/跨报表客户一致性关联 (各属地内部)"]
        direction LR
        DET_IN["同一原始数据"]
        DET_HASH["HMAC-SHA256<br/>KDF派生密钥"]
        DET_OUT["同一令牌<br/>确定性映射"]
        DET_KMS["属地独立KMS<br/>密钥不跨境同步"]
        DET_IN --> DET_HASH --> DET_OUT
        DET_HASH --> DET_KMS
    end

    subgraph L3["<b>Layer 3: 聚合令牌化</b><br/>适用: 强本地化市场跨境汇总传输 — k-匿名化(k>=5) + 差分隐私(ε=1.0~2.0)"]
        direction LR
        AGG_IN["客户A/B/C → 各自内部Token"]
        AGG_GROUP["聚合组标识<br/>Agg_Token_Group<br/>个体不可区分"]
        AGG_OUT["组级指标出境:<br/>\"该组存款合计$1.2M\""]
        AGG_IN --> AGG_GROUP --> AGG_OUT
    end

    subgraph L4["<b>Layer 4: 零知识证明令牌化 (ZKP)</b><br/>适用: 监管审计溯源——证明令牌化过程正确且无篡改"]
        direction LR
        ZKP_IN["①原始数据→Token<br/>②同步生成ZKP证明"]
        ZKP_VERIFY["③ Token+ZKP 传输"]
        ZKP_OUT["④监管验证ZKP:<br/>逻辑正确/未篡改<br/>无法反向推导原始"]
        ZKP_IN --> ZKP_VERIFY --> ZKP_OUT
    end

    L1 --> L2 --> L3 --> L4

    style L1 fill:#E3F2FD,stroke:#2E5090
    style L2 fill:#E8F5E9,stroke:#00A86B
    style L3 fill:#FFF3E0,stroke:#FF8C00
    style L4 fill:#FFE0E0,stroke:#DB0011
""", "Tokenization四层方案: FPT → 确定性令牌化 → 聚合令牌化 → ZKP (安全等级递增)")

h2("6.3 Tokenization与加密方案技术对比")
tbl(["维度", "基础加密(AES/TLS)", "FPT(格式保持)", "确定性令牌化", "聚合令牌化(k-匿名)", "ZKP令牌化"],
    [["可还原性", "✅ 可解密", "❌ (需查令牌库)", "❌", "❌ (个体不可区分)", "❌"],
     ["格式保持", "❌", "✅", "❌", "N/A", "N/A"],
     ["跨系统一致性", "✅ (同密钥)", "✅ (查令牌库)", "✅ (确定算法)", "❌", "❌"],
     ["跨境传输安全性", "⚠️ 可解密", "✅ (令牌库不跨境)", "✅ (密钥不跨境)", "✅", "✅"],
     ["审计可验证性", "⚠️ 需额外日志", "⚠️ 需令牌库日志", "⚠️", "⚠️", "✅ 自带证明"],
     ["计算开销", "低", "中", "低", "中", "高"],
     ["可作为本地化豁免", "❌", "❌", "❌", "✅ (聚合后)", "N/A"]])

h2("6.4 分市场Tokenization方案适配矩阵")
tbl(["市场分类", "推荐Tokenization层级", "说明"],
    [["**强本地化** (中/台/韩/新西/印尼/越/印/马)", "Layer 1(FPT) + Layer 3(聚合) + Layer 4(ZKP)", "本地FPT处理客户标识；聚合令牌化后出境；ZKP满足审计"],
     ["**本地副本** (日/澳/泰/菲)", "Layer 1(FPT) + Layer 2(确定性) + Layer 3(聚合)", "本地确定性令牌跨系统关联；聚合后出境"],
     ["**自由流转** (港/新)", "Layer 1(FPT) + Layer 2(确定性)", "中枢可直接处理令牌化数据"],
     ["**伊斯兰金融** (马来西亚+中东)", "全四层 + Shariah合规令牌", "额外标记Shariah合规状态令牌"],
     ["**跨境AML匹配** (全区域)", "Layer 3(聚合) + MPC密文比对", "跨市场客户关联匹配不泄露原始数据"]])

# ══════════════════════════════════════════════════════════════
# 7. IMPLEMENTATION PRIORITY
# ══════════════════════════════════════════════════════════════
h1("7. 实施优先级列表与路径规划")
h2("7.1 优先级评估方法论")
tbl(["维度", "权重", "说明"],
    [["合规风险敞口", "30%", "当前合规暴露程度、已有处罚/警告记录、监管关注度"],
     ["监管处罚力度", "20%", "可能面临的最高罚款金额、高管追责风险、牌照影响"],
     ["监管规则升级紧急度", "15%", "新规落地时间表、过渡期剩余时间"],
     ["业务影响范围", "15%", "涉及客户数、交易量、收入贡献"],
     ["技术改造成本", "10%", "系统升级难度、资源投入需求"],
     ["改造可复用性", "10%", "对区域其他市场的技术溢出价值"]])

# ── 7.2 MERMAID: Gantt/Roadmap ──
h2("7.2 三阶段实施路线图")
mermaid(r"""
gantt
    title 汇丰亚太区监管报送优化实施路线图 (2026 Q3 — 2029 Q4)
    dateFormat  YYYY-MM
    axisFormat  %Y Q%q
    tickInterval 3month

    section Phase 1: 基础夯实
    P0-1 香港中枢基础设施升级          :crit,  p01, 2026-07, 2027-03
    P0-2 澳大利亚合规整改 (3500万处罚驱动) :crit, p02, 2026-07, 2027-01
    P0-3 区域统一主数据标准制定          :       p03, 2026-10, 2027-06
    P0-4 集团统一AML报送模块搭建         :       p04, 2027-01, 2027-06

    section Phase 2: 核心升级
    P1-1 日韩台大陆法系改造 (最高难度)    :crit,  p11, 2027-07, 2028-12
    P1-2 中国大陆EAST全量明细升级        :       p12, 2027-07, 2028-06
    P1-3 东南亚新兴市场数据节点部署      :       p13, 2027-10, 2028-12
    P1-4 全链路自动化率提升至90%+        :       p14, 2027-07, 2028-12

    section Phase 3: 全量覆盖
    P2-1 南亚新兴市场                    :       p21, 2029-01, 2029-09
    P2-2 中东关联市场                    :       p22, 2029-01, 2029-09
    P2-3 伊斯兰金融专项                  :       p23, 2029-01, 2029-09
    P2-4 全区域持续优化                  :       p24, 2029-01, 2029-12
""", "三阶段实施路线图: Phase 1 基础夯实 → Phase 2 核心升级 → Phase 3 全量覆盖")

h2("7.3 Phase 1: 基础夯实 (2026Q3—2027Q2) —— 立即启动")

tbl(["优先级", "项目", "核心理由", "预计周期", "投入", "成功标准"],
    [["**P0-1** 🔴", "香港中枢基础设施升级", "香港为区域总部+自由流转市场——中枢是后续所有属地改造的前置基础设施; HKMA GDR 3.0推进中", "6-9月", "$$$$", "中枢可接收14市场汇总指标; 统一规则词典覆盖80%+通用规则"],
     ["**P0-2** 🔴", "澳大利亚合规整改", "2026年6月罚款**3500万澳元**——近年最大单笔处罚; AUSTRAC持续高压关注", "4-6月", "$$$", "AUSTRAC合规评级恢复满意; 自动化率85%+"],
     ["**P0-3**", "区域统一主数据标准", "跨系统数据映射不一致是2025香港罚款直接技术诱因; 后续所有自动化的刚性基础", "6-12月", "$$", "核心主数据在港新澳三大市场跨系统一致性>99%"],
     ["**P0-4**", "集团统一AML模块", "AML报表全亚太规则高度趋同——一次开发全区域复用，投入产出比最高", "6-9月", "$$", "统一模块覆盖12+/14市场AML报送需求"]])

h2("7.4 Phase 2: 核心升级 (2027Q3—2028Q4)")

tbl(["优先级", "项目", "核心理由", "预计周期", "投入", "成功标准"],
    [["**P1-1**", "东北亚大陆法系改造 (日韩台)", "亚太合规最高压地带; 当前自动化率<40%——汇丰最大合规盲区; 大陆法系与英美法系存在根层冲突", "12-18月", "$$$$$", "日韩台自动化率从<40%提升至80%+; 大陆法系规则池覆盖90%+"],
     ["**P1-2**", "中国大陆EAST升级", "EAST为金监总局现场检查核心抓手; 中国为最大外资行市场之一", "9-12月", "$$$", "EAST报送差错率降至同行前25%"],
     ["**P1-3**", "东南亚数据节点部署", "马/印尼/越/泰/菲均为强制本地化约束; 复用Phase 1统一架构降低成本", "12-15月", "$$$", "五市场自动化率从~50%提升至85%+"],
     ["**P1-4**", "全链路自动化90%+", "当前~60%自动化率→40%人工依赖→合规成本70%+为人工成本", "18月", "$$$", "全亚太整体自动化率≥90%"]])

h2("7.5 Phase 3: 全量覆盖 (2029Q1—2029Q4)")
tbl(["任务", "核心内容", "覆盖市场"],
    [["P2-1 南亚新兴市场", "印度 (RBI本地化强制) + 孟加拉 + 斯里兰卡 + 马尔代夫 本地节点+规则配置", "4市场"],
     ["P2-2 中东关联市场", "阿联酋/沙特(SABB)/巴林/卡塔尔 伊斯兰金融+传统银行报送", "4+市场"],
     ["P2-3 伊斯兰金融专项", "马来西亚IFSA专项 + AAOIFI标准适配 + Shariah合规事件报送模块", "马来西亚+中东"],
     ["P2-4 全区域持续优化", "基于Phase 1-2运营数据持续优化; 监管规则变更常态化适配（目标<10天）", "全部22市场"]])

# ── 7.6 Priority Matrix Table ──
h2("7.6 优先级矩阵")
tbl(["象限", "特点", "项目", "行动"],
    [["🔴 高合规风险 / 低成本", "立即启动", "P0-2 澳大利亚、P0-1 香港中枢", "Phase 1 优先实施"],
     ["🟠 高合规风险 / 高成本", "重点规划", "P1-1 日韩台、P1-2 中国大陆", "Phase 2 集中资源"],
     ["🟡 低合规风险 / 低成本", "快速收益", "P0-3 主数据标准、P0-4 AML统一模块", "Phase 1 同步推进"],
     ["🟢 低合规风险 / 高成本", "渐进覆盖", "P1-3 东南亚、P2系列", "Phase 2-3 渐进实施"]])

h2("7.7 关键里程碑")
tbl(["时间节点", "里程碑", "关键交付物"],
    [["**2026 Q4**", "香港中枢基础设施投产", "GCP双活中枢上线; 统一规则词典V1.0"],
     ["**2027 Q1**", "澳大利亚合规整改完成", "AUSTRAC合规评级恢复; 自动化率85%+"],
     ["**2027 Q2**", "统一主数据标准+AML模块投产", "核心主数据标准文档; 统一AML引擎上线"],
     ["**2027 Q4**", "日韩大陆法系规则引擎上线", "大陆法系规则池V1.0; 韩国实时报送链路投产"],
     ["**2028 Q2**", "中国大陆EAST升级完成", "EAST V3.0接口上线; 差错率达标"],
     ["**2028 Q4**", "全亚太自动化率达90%", "全链路自动化平台上线"],
     ["**2029 Q4**", "全量市场覆盖完成", "全部22市场纳入统一报送治理体系"]])

# ══════════════════════════════════════════════════════════════
# 8. CRITICAL SUCCESS FACTORS
# ══════════════════════════════════════════════════════════════
h1("8. 关键成功因素 (Critical Success Factors)")

csfs = [
    ("CSF 1: 集团高层持续且可见的承诺与授权", "⭐⭐⭐⭐⭐", "集团COO/CDO",
     "区域统筹权正式文件发布；专项预算批复",
     "亚太区监管报送体系优化的本质是重塑治理架构——涉及集团总部-区域总部-属地三层权力重新分配。若无高层持续授权→属地各自为政→标准不统一→合规风险不降反升。",
     "集团层面明确亚太区COO/CDO为项目唯一执行负责人(SPA)；授予区域总部跨属地合规标准统筹权；将报送优化纳入各市场CEO/COO年度KPI"),
    ("CSF 2: 双法系规则引擎的成功落地", "⭐⭐⭐⭐⭐", "区域CTO/CIO",
     "大陆法系规则池覆盖率>90%；新规则适配<10天",
     "汇丰现有英美法系架构与东北亚大陆法系监管要求的根层冲突是最大结构性缺陷。双法系规则引擎是解决这一矛盾的唯一可行技术方案。",
     "2026 Q4前完成日韩台监管规则完整翻译和分级分析；设计\"共性统一覆盖+差异单独适配\"分层逻辑；建立属地规则版本管理机制"),
    ("CSF 3: 数据治理——\"先治后报\"", "⭐⭐⭐⭐⭐", "区域CDO",
     "核心主数据跨系统一致性>99%",
     "现有架构最基础缺陷是源头数据质量问题。不解决→自动化率提升后\"垃圾进垃圾出\"→错误数据更快提交监管→更严重处罚。",
     "强制推行统一主数据标准；建立跨系统数据映射垂直管控；部署数据质量校验规则引擎在前端拦截问题数据；全面清洗历史数据"),
    ("CSF 4: 属地监管关系管理与信任建设", "⭐⭐⭐⭐", "各市场COO",
     "过渡期零监管处罚",
     "优化过程中不可避免新老系统并行期——报送可能出现短暂波动。属地监管的谅解与配合是过渡期平稳的关键。",
     "各市场COO/CIO亲自向监管主动沟通优化计划；建立正式联络窗口；提前报备并行期波动争取缓冲；定期展示优化成果建立信任"),
    ("CSF 5: 人才与组织能力保障", "⭐⭐⭐⭐", "区域HR+COO",
     "CoE成立；关键岗位到位率>90%",
     "22个市场、三大法系、数十种报送标准——需要一支理解银行业务、熟悉监管规则、精通数据技术的复合型团队。",
     "成立亚太区监管报送卓越中心(CoE)设于香港；配备大陆法系专家+伊斯兰金融合规专家+数据架构师+隐私计算工程师；各属地专职报送技术团队"),
    ("CSF 6: 分阶段交付、快速验证、持续迭代", "⭐⭐⭐⭐", "项目总监",
     "每6个月可演示成果",
     "全区域改造周期3年+，监管规则持续变化。若\"大爆炸\"式交付→建成即落后。",
     "每6个月必须有可演示的阶段性成果；选择香港+澳大利亚先行先试快速验证；建立月度区域合规状态Review机制"),
    ("CSF 7: 合规举证能力的系统性建设", "⭐⭐⭐⭐⭐", "区域合规+CTO",
     "监管问询24小时内出具溯源证明",
     "新一代监管核心标准已从\"报表格式正确\"转变为\"全链路过程可审计可溯源\"。不能举证=能力无法转化为合规安全。",
     "数据血缘+加密日志+操作日志三位一体不可篡改归档；建立\"一键式\"核查响应；分层血缘(本地完整明细+中枢指标级汇总)；留存期限7-20年"),
]

tbl(["CSF", "关键度", "负责角色", "衡量指标", "为什么关键", "具体要求"],
    [[c[0], c[1], c[2], c[3], c[4], c[5]] for c in csfs])

# ══════════════════════════════════════════════════════════════
# 9. REFERENCES
# ══════════════════════════════════════════════════════════════
h1("9. 参考文件与依据清单")

h2("9.1 汇丰集团官方公开文件 (13项)")
tbl(["序号", "文件/来源", "涉及内容"],
    [["1", "HSBC Holdings plc Annual Report and Accounts 2025", "亚太区业务规模、市场覆盖、财务数据"],
     ["2", "HSBC Group Simplified Structure Chart (2025/2026)", "亚太区子公司架构、股权持有关系"],
     ["3", "The Hongkong & Shanghai Banking Corp. - Pillar 3 Disclosures (2025)", "香港主体资本充足率、流动性、风险敞口披露"],
     ["4", "HSBC Bank Australia Limited - Pillar 3 Disclosures (2025)", "澳大利亚审慎报送架构"],
     ["5", "HSBC Bank (Singapore) Limited - Pillar 3 Disclosures (2025)", "新加坡审慎报送架构、MAS600"],
     ["6", "HSBC Bank (China) Company Limited - Annual Report (2025)", "中国业务规模、监管合规框架"],
     ["7", "HSBC Group Regulatory Reporting System Upgrade Report (2024)", "报送自动化率~60%、合规成本增速>收入增速"],
     ["8", "HSBC APAC Investor & Analyst Strategy Seminar (May 2026)", "客群战略\"高价值、强跨境、易合规\""],
     ["9", "HSBC Malaysia - Islamic Banking License Disclosure (2007)", "HSBC Amanah Malaysia Berhad成立资质"],
     ["10", "HSBC Singapore - Enterprise Banking Strategy", "创新型企业客户服务专项团队"],
     ["11", "HSBC Philippines - Retail Banking Service Adjustment Notice (2024)", "停止开放新非卓越理财账户"],
     ["12", "HSBC China / HSBC Hong Kong - Premier Elite International Pass", "卓越理财·尊尚国际通跨境服务"],
     ["13", "HSBC HK / HSBC Philippines - \"区域内极速汇\"", "港马新菲跨境零手续费实时到账"]])

h2("9.2 监管机构官方文件 (35项)")
tbl(["序号", "文件/来源", "涉及内容"],
    [["14", "HKMA - Banking (Disclosure) Rules (BDR)", "香港银行业披露规则"],
     ["15", "HKMA - Financial Institutions (Resolution) (LAC) Rules", "香港LAC规则（独有）"],
     ["16", "HKMA & SFC - Joint Enforcement Action against HSBC (Aug 2025)", "研究报告披露违规罚款420万港元"],
     ["17", "MAS Notice 637 - Risk-Based Capital Adequacy Requirements", "新加坡资本充足率要求"],
     ["18", "MAS Notice 651 - Liquidity Coverage Ratio", "新加坡流动性要求"],
     ["19", "PBOC/NFRA - 《商业银行资本管理办法》", "中国资本管理"],
     ["20", "NFRA - EAST数据标准", "中国EAST全量明细报送"],
     ["21", "SAFE - 跨境资金流动监测相关要求", "中国跨境外汇报送"],
     ["22", "APRA - Prudential Standard APS 330 (Public Disclosure)", "澳大利亚审慎披露"],
     ["23", "APRA - CPS 234 Information Security", "澳大利亚信息安全标准"],
     ["24", "AUSTRAC - AML/CTF Act", "澳大利亚反洗钱法"],
     ["25", "Federal Court of Australia - ASIC v HSBC Bank Australia (Jun 2026)", "反诈报送缺陷罚款3500万澳元"],
     ["26", "BNM - Risk-Based Capital Adequacy Framework", "马来西亚资本充足框架"],
     ["27", "BNM - Financial Services Act 2013 (FSA)", "马来西亚传统银行法"],
     ["28", "BNM - Islamic Financial Services Act 2013 (IFSA)", "马来西亚伊斯兰银行法"],
     ["29", "BNM - Policy Document on Financial Reporting for Islamic Banking (Apr 2022)", "MFRS+Shariah合同披露"],
     ["30", "BNM - Policy Document on Operational Risk Reporting (Jan 2026)", "ORR: LED/KRI/SA"],
     ["31", "BNM - Policy Document on Islamic Banking Window (Nov 2024)", "伊斯兰银行窗口修订"],
     ["32", "OJK - Banking Capital Adequacy Regulation", "印尼资本充足率管理"],
     ["33", "OJK - GR71 Electronic Transaction Regulation", "印尼数据本地化强制令"],
     ["34", "BOT - Capital Adequacy Disclosure Notification", "泰国资本充足披露"],
     ["35", "SBV - Capital Adequacy Regulation", "越南资本充足管理"],
     ["36", "Vietnam - Law on Cybersecurity (Article 26)", "越南数据本地化强制"],
     ["37", "BSP - Banking Capital Adequacy Regulation", "菲律宾资本充足"],
     ["38", "Japan FSA - Banking Act", "日本银行法"],
     ["39", "Japan BOJ - FX Transaction Ledger Retention Rules", "日本外汇台账留存"],
     ["40", "South Korea FSS - Financial Information Security Guidelines", "韩国金融信息安全"],
     ["41", "South Korea - Personal Information Protection Act", "韩国个人信息保护法"],
     ["42", "Taiwan FSC - Financial Information Security Regulations", "台湾金融资讯安全规范"],
     ["43", "Taiwan - Cross-Strait Financial Interaction Regulations", "两岸金融往来监管"],
     ["44", "RBNZ - Prudential Information Security Rules", "新西兰审慎信息安全"],
     ["45", "RBI - Payment Data Localisation Mandate", "印度支付数据本地化"],
     ["46", "PRC - 《网络安全法》《个人信息保护法》", "中国数据安全"],
     ["47", "PRC - 《促进和规范数据跨境流动规定》", "匿名化聚合数据豁免安全评估"],
     ["48", "AAOIFI - Financial Accounting & Shariah Governance Standards", "伊斯兰金融国际标准"]])

h2("9.3 行业研究机构报告 (8项)")
tbl(["序号", "文件/来源", "涉及内容"],
    [["49", "Dataintelo - HK Banking Regulatory Reporting Automation Market Report", "香港报送自动化行业对标"],
     ["50", "PW Consulting - APAC Financial Institution Compliance Trend Report", "合规成本增速>税前利润增速"],
     ["51", "Speedydd - APAC Financial Institution Compliance Trends", "监管规则碎片化趋势"],
     ["52", "Nasdaq - APAC Financial Institution Regulatory Reporting Trends", "新一代报送标准技术约束"],
     ["53", "Risk.net - APAC Head Banks Regulatory Reporting Architecture Benchmarking", "汇丰vs国际同业架构对标"],
     ["54", "Risk.net - APAC Banking Data Governance & Reporting Architecture Report", "数据治理行业最佳实践"],
     ["55", "Reportify - Banking Industry Comparative Analysis", "汇丰亚太报送行业位置"],
     ["56", "CICC (中金公司) - Banking Sector Report", "头部银行报送合规差异"]])

h2("9.4 国际标准与框架 (8项)")
tbl(["序号", "标准/框架", "涉及领域"],
    [["57", "Basel III Final Reform", "巴塞尔III资本/流动性/杠杆率"],
     ["58", "BCBS 239 - Risk Data Aggregation and Risk Reporting", "数据治理原则"],
     ["59", "FATF - International Standards on Combating Money Laundering", "反洗钱国际标准"],
     ["60", "AAOIFI - Financial Accounting Standards (FAS)", "伊斯兰金融会计"],
     ["61", "AAOIFI - Shariah Governance Standards", "Shariah治理"],
     ["62", "ISSB - Climate-Related Disclosures (IFRS S2)", "ESG与气候风险披露"],
     ["63", "NIST SP 800-38G - Format-Preserving Encryption", "格式保持加密(FF1算法)"],
     ["64", "OpenLineage - Data Lineage Standard", "数据血缘标准框架"]])

# ══════════════════════════════════════════════════════════════
# APPENDIX
# ══════════════════════════════════════════════════════════════
h1("附录")

h2("Appendix A: 汇丰亚太区近年主要合规处罚案例")
tbl(["时间", "市场", "监管机构", "事由", "处罚金额/措施"],
    [["2025年8月", "香港", "HKMA+SFC", "2013-2021年间逾4200份上市证券研究报告未披露/错误披露投行关联关系", "罚款420万港元"],
     ["2026年6月", "澳大利亚", "Federal Court", "2020-2024年反诈交易调查处理严重滞后、风控管控存在系统性漏洞、客户申诉流程存在重大缺陷", "罚款**3500万澳元**"],
     ["近年", "马来西亚", "BNM", "企业客户跨境贸易证明材料报送内容不全、数据溯源链路不完整", "公开警告+专项整改"],
     ["近年", "印度尼西亚", "OJK", "反洗钱可疑交易报告提交不及时", "公开警告+限期整改"],
     ["近年", "越南", "SBV", "报送数据溯源链路不完整、合规支撑材料缺失", "限期整改+合规评级下调"]])

h2("Appendix B: 监管报送标准代际演进")
tbl(["代际", "时期", "特征", "汇丰当前状态", "行业头部状态"],
    [["**第一代**", "1990s-2010", "结果导向型：纸质/PDF报表、汇总指标、年报/半年报、人工提交", "部分新兴市场仍在此阶段", "已全部升级"],
     ["**第二代**", "2010-2020", "标准化报表型：电子报表、XML/CSV格式、API传输、部分自动化", "**多数市场当前状态**", "已开始向第三代过渡"],
     ["**第三代**", "2020-现在", "过程导向型：细粒度交易级数据、全链路溯源、实时/准实时报送、不可篡改审计日志", "仅港/新成熟市场部分具备", "**全面推进中**"]])

para("> **GAP分析**: 汇丰在新兴市场与行业头部存在1-2代标准差距——这也是本报告建议Phase 1即启动中枢升级的核心原因。")

h2("Appendix C: 各市场数据本地存储法规完整依据清单")
tbl(["市场", "法规/政策文件", "核心条款", "类别"],
    [["中国大陆", "《网络安全法》《个人信息保护法》《金融机构客户尽职调查和交易记录保存管理办法》", "境内产生的全部客户身份资料、交易明细、反洗钱底层数据必须境内服务器存储", "强强制"],
     ["中国台湾", "金管会金融资讯安全规范、个人资料保护法、两岸金融往来监管办法", "新台币账户交易、两岸跨境资金明细全量境内留存；两岸专项原始台账禁止出境", "强强制"],
     ["韩国", "个人信息保护法、BOK外汇监管数据留存规则、FSS金融资讯安全指引", "韩元外汇交易、财阀关联交易原始数据必须本地留存；仅聚合指标可跨境", "强强制"],
     ["新西兰", "RBNZ审慎信息安全规则、隐私法、本地法人资本隔离制度", "本地法人底层业务数据物理隔离；禁止境外集中存储原始明细", "强强制"],
     ["印度尼西亚", "OJK金融监管条例、GR71电子交易条例", "全部本地客户交易、信贷、外汇、反洗钱明细仅允许印尼境内服务器存储", "强强制"],
     ["越南", "《越南网络安全法》第26条、SBV银行数据管理规定", "越南盾交易、外资企业授信原始明细境内存储；出境需公安部审批", "强强制"],
     ["印度", "RBI支付数据本地化强制通知、银行业信息安全指引", "支付类数据100%境内存储；卢比清算、FDI底层明细无监管许可不得出境", "强强制"],
     ["马来西亚", "BNM金融数据安全指引、伊斯兰金融业务数据管理规则", "马币本地交易、伊斯兰金融专项台账境内留存；原始明细不得长期境外存放", "强强制"],
     ["日本", "FSA信息安全指引、BOJ外汇交易台账留存规则", "全量交易台账在日本境内留存完整副本（非强制仅本地存储但要求完整副本）", "有条件副本"],
     ["澳大利亚", "APRA CPS 234、AUSTRAC反洗钱数据留存规则", "客户信贷、跨境IFT、房贷明细保留完整本地副本；监管优先调取境内存储", "有条件副本"],
     ["泰国", "BOT数据管理规范、个人数据保护法", "大额现金CTR、进出口贸易融资台账留存泰国本地副本；仅统计汇总表可境外", "有条件副本"],
     ["菲律宾", "BSP银行业数据指引、国家隐私委员会规则", "海外侨汇、跨境贸易原始明细本地留存完整副本；监管不可仅调取境外数据", "有条件副本"],
     ["中国香港", "HKMA资讯科技风险管理指引、打击洗钱条例", "无数据本地化强制条款——**唯一可自由跨境流转市场之一**", "自由流转"],
     ["新加坡", "MAS科技风险管理指引、PDPA个人数据保护法", "不强制金融数据本地存储——**可作为亚太统一报送数据中枢**", "自由流转"]])

h2("Appendix D: 术语缩略语对照表")
tbl(["缩写", "全称", "中文"],
    [["AML", "Anti-Money Laundering", "反洗钱"],
     ["APRA", "Australian Prudential Regulation Authority", "澳大利亚审慎监管局"],
     ["AUSTRAC", "Australian Transaction Reports and Analysis Centre", "澳大利亚交易报告与分析中心"],
     ["BNM", "Bank Negara Malaysia", "马来西亚国家银行"],
     ["BOP", "Balance of Payments", "国际收支"],
     ["BOT", "Bank of Thailand", "泰国银行"],
     ["BSP", "Bangko Sentral ng Pilipinas", "菲律宾中央银行"],
     ["CDC", "Change Data Capture", "变更数据捕获"],
     ["CRS", "Common Reporting Standard", "共同汇报标准"],
     ["CSF", "Critical Success Factor", "关键成功因素"],
     ["CTR", "Cash Transaction Report", "大额现金交易报告"],
     ["EAST", "Examination and Analysis System Technology", "检查分析系统（中国）"],
     ["FATCA", "Foreign Account Tax Compliance Act", "海外账户税收合规法案（美国）"],
     ["FHE", "Fully Homomorphic Encryption", "全同态加密"],
     ["FPT", "Format-Preserving Tokenization", "格式保持令牌化"],
     ["FSA", "Financial Services Agency", "日本金融厅"],
     ["FSS", "Financial Supervisory Service", "韩国金融监督院"],
     ["GCP", "Google Cloud Platform", "谷歌云平台"],
     ["GDR", "Granular Data Reporting", "颗粒化数据报送"],
     ["G-SIBs", "Global Systemically Important Banks", "全球系统重要性银行"],
     ["HKMA", "Hong Kong Monetary Authority", "香港金融管理局"],
     ["IFSA", "Islamic Financial Services Act 2013", "伊斯兰金融服务法案（马来西亚）"],
     ["IFT", "International Funds Transfer", "跨境资金划转"],
     ["KMS", "Key Management Service", "密钥管理服务"],
     ["KYC", "Know Your Customer", "了解你的客户"],
     ["LCR", "Liquidity Coverage Ratio", "流动性覆盖率"],
     ["MAS", "Monetary Authority of Singapore", "新加坡金融管理局"],
     ["MPC", "Multi-Party Computation", "多方安全计算"],
     ["NFRA", "National Financial Regulatory Administration", "国家金融监督管理总局（中国）"],
     ["NSFR", "Net Stable Funding Ratio", "净稳定资金比例"],
     ["ODS", "Operational Data Store", "操作数据存储"],
     ["OJK", "Otoritas Jasa Keuangan", "印度尼西亚金融服务管理局"],
     ["PBOC", "People's Bank of China", "中国人民银行"],
     ["PETs", "Privacy-Enhancing Technologies", "隐私增强技术"],
     ["RBI", "Reserve Bank of India", "印度储备银行"],
     ["RBNZ", "Reserve Bank of New Zealand", "新西兰储备银行"],
     ["RWA", "Risk-Weighted Assets", "风险加权资产"],
     ["SAFE", "State Administration of Foreign Exchange", "国家外汇管理局（中国）"],
     ["SBV", "State Bank of Vietnam", "越南国家银行"],
     ["STR", "Suspicious Transaction Report", "可疑交易报告"],
     ["TDE", "Transparent Data Encryption", "透明数据加密"],
     ["ZKP", "Zero-Knowledge Proof", "零知识证明"]])

h2("Appendix E: 版本记录")
tbl(["版本", "日期", "作者", "变更说明"],
    [["V1.0", "2026-07-25", "亚太区监管报送专家顾问组", "初始版本——覆盖全亚太22市场，含Mermaid架构图/Python数据图表/完整表格"]])

para("---\n\n"
     "> **免责声明**：本报告所有信息和数据均基于汇丰集团公开披露文件、各市场监管机构官方公告、行业独立研究机构公开报告整理汇编。"
     "报告中涉及的业务规模估计和对比数据来自公开渠道，仅供战略参考，精确数据需以汇丰集团内部管理信息系统为准。"
     "本报告不构成任何投资、经营决策建议。\n\n"
     "---\n\n"
     "*本报告由亚太区监管报送专家顾问组编制，仅供汇丰集团内部使用。*\n"
     "*© HSBC Holdings plc 2026. All Rights Reserved. CONFIDENTIAL.*")

# ══════════════════════════════════════════════════════════════
# Write .ipynb
# ══════════════════════════════════════════════════════════════
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f"✅ Notebook written → {OUT}")
print(f"   Total cells: {len(nb['cells'])}")
