# HSBC APAC Regulatory Reporting — Consulting Report (中文版)

汇丰集团亚太区监管报送体系优化咨询报告。面向亚太区 COO、CDO/CIO 及各市场管理层，覆盖 22 个亚太市场的监管报送要求全景分析。

## 快速开始

```bash
./build_all.sh
```

生成 `HSBC-AME-RR-summary-cn.pdf`。

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
cn/
├── README.md                          # 本文件
├── build_all.sh                       # 一键构建脚本 (charts + mermaid + PDF)
├── generate_charts.py                 # matplotlib 图表 → img/
├── number-figures.lua                 # Pandoc 过滤器 (章节编号/图表标题)
├── hsbc-template.latex                # HSBC 品牌 LaTeX 模板
├── HSBC-AME-RR-summary-cn.md          # 单文件 Markdown 源 (回退兼容)
├── HSBC-AME-RR-summary-cn.pdf         # (生成) 最终 PDF
├── chapters/                          # 分章文件 (優先讀取，方便編輯)
│   ├── 00-frontmatter.md              #   标题 + 元数据
│   ├── 01-1-执行摘要.md                #   §1 执行摘要
│   ├── 02-2-汇丰亚太区市场覆盖与业务全景.md #   §2 市场覆盖
│   ├── 03-3-亚太区监管要求五级分类汇总.md   #   §3 监管分类
│   ├── 04-4-数据本地存储与跨境约束全景分析.md # §4 数据本地存储
│   ├── 05-5-分布式数据处理架构方案.md       #   §5 分布式架构
│   ├── 06-6-数据-tokenization-技术方案.md  #   §6 Tokenization
│   ├── 07-7-实施优先级列表与路径规划.md      #   §7 实施优先级
│   ├── 08-8-关键成功因素-...md              #   §8 关键成功因素
│   ├── 09-9-参考文件与依据清单.md            #   §9 参考文献
│   └── 10-附录.md                       #   附录 A–E
└── img/
    ├── chart1_business_mix.png        # Python 图表
    ├── chart2_size_vs_automation.png
    ├── chart3_reg_intensity.png
    └── mermaid/
        ├── diagram_01.mmd ~ 07.mmd    # Mermaid 源文件 (中文)
        └── diagram_01.png ~ 07.png    # Mermaid 架构图 (渲染产物)
```

> 如果有 `chapters/`，`build_all.sh` 会優先讀取分章文件；否则回退读取 `HSBC-AME-RR-summary-cn.md`。

## 构建流程

```
generate_charts.py    build_all.sh (mmdc)    build_all.sh (pandoc)
      │                      │                      │
      │ matplotlib            │ mermaid-cli          │ pandoc + xelatex
      ▼                      ▼                      ▼
  img/chart*.png      img/mermaid/diagram_*.png    .md ──► .pdf
                                                   (经 number-figures.lua
                                                   + hsbc-template.latex)
```

1. **`generate_charts.py`** — 用 matplotlib 生成 3 张统计图
2. **`mmdc` (mermaid-cli)** — 将 `img/mermaid/*.mmd` 渲染为 PNG
3. **`pandoc + xelatex`** — 合并分章 → 预处理 emoji/Unicode → LaTeX → PDF

## 使用方法

```bash
./build_all.sh              # 全量构建 (charts + mermaid + PDF)
./build_all.sh --pdf-only   # 只构建 PDF (跳过 charts 和 mermaid)
./build_all.sh --clean      # 清理构建产物
```

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
| §9 参考文献 | 64 项引用 (汇丰官方/监管文件/行业报告/国际标准) |
| 附录 | 处罚案例、标准演进、法规清单、术语表 |

## 常见问题

**Q: 构建报错 `mmdc: command not found`**

```bash
npm install -g @mermaid-js/mermaid-cli
```

**Q: PDF 中文显示为方块**

安装 CJK 字体：`brew install --cask font-noto-sans-cjk-sc`

**Q: 只改动了 markdown 不想重新生成图表和 mermaid**

```bash
./build_all.sh --pdf-only
```

**Q: LaTeX 报错 `\pandocbounded undefined`**

pandoc 版本需 ≥ 3.0。升级：`brew upgrade pandoc`
