# HSBC APAC Regulatory Reporting — Consulting Report

汇丰集团亚太区监管报送体系优化咨询报告。面向亚太区 COO、CDO/CIO 及各市场管理层，覆盖 22 个亚太市场的监管报送要求全景分析。

## 快速开始

```bash
./build_all.sh
```

生成 `HSBC-APAC-Regulatory-Reporting-Consulting-Report-FINAL.pdf`。

## 前置依赖

| 工具 | 安装 (macOS) |
|------|-------------|
| pandoc ≥ 3.0 | `brew install pandoc` |
| XeLaTeX (MacTeX) | `brew install mactex-no-gui` |
| CJK 字体 | `brew install --cask font-noto-sans-cjk-sc` |
| Python 3 + matplotlib | `pip3 install matplotlib numpy` |
| mermaid-cli | `npm install -g @mermaid-js/mermaid-cli` |

## 目录结构

```
hsbc-regulatorty-reporting/
├── README.md                          # 本文件
├── build_all.sh                       # 一键构建脚本 (charts + mermaid + PDF)
├── generate_charts.py                 # 生成 matplotlib 图表 → img/
├── build_report.py                    # 渲染 mermaid 图表 + 组装 markdown
├── number-figures.lua                 # Pandoc 过滤器 (章节去重/图表编号)
├── hsbc-template.latex                # HSBC 品牌 LaTeX 模板
├── HSBC-APAC-...-Report.ipynb         # Jupyter Notebook 源文件
├── HSBC-APAC-...-Report-FINAL.md      # (生成) 最终 Markdown
├── HSBC-APAC-...-Report-FINAL.pdf     # (生成) 最终 PDF
├── img/
│   ├── chart1_business_mix.png        # Python 图表
│   ├── chart2_size_vs_automation.png
│   ├── chart3_reg_intensity.png
│   └── mermaid/
│       ├── diagram_01.png ~ 07.png    # Mermaid 架构图
│       └── diagram_01.mmd ~ 07.mmd    # Mermaid 源文件
└── tbd/                               # 遗留/参考文件
    ├── build.sh                       # 旧构建脚本
    ├── build_notebook.py              # 旧 notebook 生成脚本
    ├── fix_assets.py                  # 一次性文件名清理脚本
    ├── regulatory-reporting.md        # 原始分析报告 (基础)
    ├── reg-rprt-cyber.md              # 原始分析 (加密技术)
    ├── reg-rprt-texonomy.md           # 原始分析 (报表分类)
    ├── reg-rprt-xb.md                 # 原始分析 (数据本地存储)
    ├── reg-rprt2.md                   # 原始分析 (日韩台新)
    └── reg-rprt3.md                   # 原始分析 (MENAT 扩展)
```

## 构建流程

```
generate_charts.py          build_report.py           build_all.sh
      │                          │                        │
      │ matplotlib                │ mermaid-cli (mmdc)    │ pandoc + xelatex
      │                          │                        │
      ▼                          ▼                        ▼
  img/chart*.png           img/mermaid/              .md ──► .pdf
                           diagram_*.png             (经 number-figures.lua
                                                     + hsbc-template.latex)
```

1. **`generate_charts.py`** — 读取内嵌数据，用 matplotlib 生成 3 张统计图 (柱状/气泡/分组柱)
2. **`build_report.py`** — 从 `.ipynb` 提取 mermaid → `mmdc` 渲染 PNG → 替换代码块为图片引用 → 输出 `.md`
3. **`build_all.sh`** — 预处理 emoji/Unicode → pandoc + number-figures.lua + hsbc-template.latex → PDF

## 报告内容

| 章节 | 内容 |
|------|------|
| §1 执行摘要 | 核心发现、战略建议 |
| §2 市场覆盖 | 22 个亚太市场业务全景、客群矩阵、业务结构图表 |
| §3 监管分类 | 五级分类标准、14 核心市场逐市场拆解、伊斯兰金融双轨制 |
| §4 数据本地存储 | 三类强制分级、跨境传输白名单/黑名单 |
| §5 分布式架构 | 五层架构方案、AML MPC 跨市场筛查流程 |
| §6 Tokenization | 四层令牌化方案 (FPT/确定性/聚合/ZKP) |
| §7 实施优先级 | 三阶段路线图、优先级矩阵、关键里程碑 |
| §8 关键成功因素 | 7 项 CSF 矩阵 |
| §9 参考文献 | 78 项引用 (汇丰官方/监管文件/行业报告/国际标准) |
| 附录 | 处罚案例、标准演进、法规清单、术语表 |

## 常见问题

**Q: 构建报错 `mmdc: command not found`**

```bash
npm install -g @mermaid-js/mermaid-cli
```

**Q: PDF 中文显示为方块**

安装 CJK 字体：`brew install --cask font-noto-sans-cjk-sc`

**Q: 只改动了 markdown 不想重新生成图表**

```bash
./build_all.sh --pdf-only
```

**Q: LaTeX 报错 `\pandocbounded undefined`**

pandoc 版本需 ≥ 3.0。升级：`brew upgrade pandoc`
