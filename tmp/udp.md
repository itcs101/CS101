**统一大数据平台监管报送架构设计**

覆盖 YBT / EAST / 1104 / BOP / LVT 五报送

基于 GCP + Collibra + DQ Hub + OpenLineage

**第一部分：统一数仓分层设计（ODS → DWD → DWS → ADS）**

核心原则：ODS 分源、DIM 全局共享、DWD 按业务过程建模（Kimball）、DWS
按监管主题汇总、ADS 按监管机构隔离。

**1. ODS（Operational Data Store）— 贴源层**

定位：数仓入口，完整镜像源系统数据，不加业务逻辑，满足监管“数据可追溯、可重跑”。

**典型接入源表**

|  |  |  |
|----|----|----|
| **源系统** | **ODS 表例** | **主要内容** |
| 核心系统 | ods_core_trans_di | 存取款交易、账户余额、币种、开/销户日期 |
| 信贷系统 | ods_loan_contract_di | 借据号、合同金额、期限、利率、担保方式、放款状态 |
| 国际结算 | ods_forex_swift_di | SWIFT 报文解析后的涉外收付款记录 |
| 理财系统 | ods_wealth_hold_di | 产品信息、客户持有份额、净值 |
| CIF | ods_cust_info_df | 客户号、证件类型/号、客户性质、行业代码 |

**ODS 设计要点**

• 按源系统分 schema（ods_core / ods_loan / ods_forex / ods_cif /
ods_wealth / ods_gl）

• 字段名/类型尽量与源库一致，PARTITIONED BY (dt STRING)

• 仅加审计字段（\_load_time、\_batch_id、\_src_sys）

• 保留原始币种原金额，供监管核查溯源

**2. DIM（公共一致性维度层）**

全行唯一版本，SCD Type2 拉链表，码值映射 →
监管标准（一表通/EAST/1104/BOP 共用）。

|  |  |  |
|----|----|----|
| **维度表** | **关键字段** | **说明** |
| dim_cust（SCD2） | customer_key、证件类型/号、客户性质、行业代码、常驻国别、生效/失效时间 | 保留客户信息历史变更 |
| dim_acct | 账号、账户性质、币种、开户机构key | 账户维度 |
| dim_org | org_key、机构号、金融机构标识码、所属分行 | 机构维度 |
| dim_prod | prod_key、产品类型、会计科目映射 | 产品维度 |
| dim_industry | GB/T + 一表通/1104 映射 | 贷款投向 |
| dim_country_code | ISO、外管局国别码 | BOP/JW 标识 |
| dim_dict_reg | 行内码 → 监管码（担保方式/五级分类/证件类型等） | 统一码值映射 |

**3. DWD（Data Warehouse Detail）— 标准化明细事实层**

按业务过程（Business Process）建模，粒度 = 最小业务事件。币种存原币 +
折合 CNY + USD + 汇率。

**核心 DWD 表**

|                         |                                                  |
|-------------------------|--------------------------------------------------|
| **DWD 表**              | **内容 / 用途**                                  |
| dwd_aml_trans_detail_di | 所有资金交易明细 → 人行大额反洗钱 + EAST + 1104  |
| dwd_fx_payment_di       | 涉外收付款明细 → BOP + EAST 涉外 + 1104 涉外校验 |
| dwd_loan_contract_di    | 贷款合同/借据 → 一表通 + EAST + 1104             |
| dwd_loan_disburse_di    | 放款流水                                         |
| dwd_loan_repay_di       | 还本/付息/逾期/核销                              |
| dwd_deposit_acct_di     | 存款账户余额/属性 → 一表通 + EAST + 1104         |
| dwd_interbank_deal_di   | 同业拆放/买入返售 → 一表通 + 1104                |
| dwd_wealth_hold_di      | 理财持有 → 一表通 + EAST                         |

**DWD 关键字段设计（应对交易拆分场景）**

以联名账户、SWIFT 拆笔等场景为例，DWD 需额外存储：

|  |  |  |
|----|----|----|
| **字段** | **类型** | **说明** |
| biz_event_no | 业务事件归并号 | 联名两行同号、SWIFT 拆笔同行 |
| trans_amt | 会计份额金额（联名 A=5 万） | EAST 用此列 |
| trans_amt_event | 监管业务口径金额（联名整笔=10 万） | BOP/LVT/1104 用此列 |
| share_ratio | 本行占 event 比例（50%） | 联名账户专用 |
| customer_key / related_cust_key | 双客户挂接 | 联名 A/B 各进各栏（1104） |
| trans_type | PRINCIPAL / FEE / COR_BANK | SWIFT 拆笔归并 |

**DWD 层铁律：所有监管报送只许引用 DWD（或 DIM），不许回抽 ODS。**

**4. DWS（Data Warehouse Summary）— 监管主题汇总层**

按监管主题（而非按报送）轻度/中度聚合，供五报送 + 内控看板复用。

|  |  |
|----|----|
| **DWS 表** | **分组键 / 指标** |
| dws_loan_org_monthly_sum | month, org, prod, five_class, industry → 贷款余额、累放、累收、逾期、不良 |
| dws_deposit_org_daily_sum | biz_date, org, deposit_type, ccy → 余额、账户数 |
| dws_fx_cust_daily_sum | biz_date, customer, direction → 涉外收付折 USD/CNY |
| dws_aml_cust_daily_trans_sum | biz_date, customer, is_cash → 现金/转账日累计（AML 阈值判定） |
| dws_interbank_org_monthly_sum | month, org, deal_type → 同业拆放/回购余额 |

**5. ADS / 监管集市 — 按监管机构隔离**

每个监管报送独立 schema，只做字段映射 + 范围过滤 + DQ 校验 + 报文生成。

|  |  |  |
|----|----|----|
| **报送** | **Schema** | **典型表 / 内容** |
| 人行大额反洗钱 | ads_aml | dm_aml_large_txn_report |
| BOP（外管局） | ads_bop | dm_bop_jbxx_pending（基础信息）、dm_bop_sbxx_pending（申报信息）、dm_bop_jgb01（单位基本情况表） |
| 一表通（金监局） | ads_ybt | dm_ybt_loan_contract、dm_ybt_cust_info、dm_ybt_deposit |
| EAST | ads_east | dm_east_acct、dm_east_trans、dm_east_loan、dm_east_fx |
| 1104 | ads_1104 | dm_1104_index、dm_1104_schedule（指标宽表） |

ADS → 质控 → 可信区 → 报文/文件 → 报送平台

**第二部分：交易拆分场景与五报送口径差异**

ODS → DWD
段，源系统为会计分录或报文落地，常把一笔“业务意义上的交易”拆成多条 ODS
记录。DWD 必须加“归并号 + 业务口径金额 + 联名双
customer”三件套，让五个报送各取所需。

**1. 联名账户（USD 10 万跨境汇入，夫妻 50% 各持）**

|  |  |  |  |
|----|----|----|----|
| **报送** | **金额口径** | **金额取值** | **特殊逻辑** |
| BOP | 按 event 归并 | trans_amt_event（10 万） | 主持有人申报；(JW) 前缀 |
| LVT | 按 event 判阈值 | trans_amt_event ≥ 1 万 USD | 明细仍按份额两行报 |
| EAST | 按账户份额 | trans_amt（5 万） | biz_event_no 关联原笔 |
| 1104 | 按 customer_key 分组 | A 居民 5 万 + B 非居民 5 万 | 各进各栏 |

**2. 其他拆分场景速览**

|  |  |  |
|----|----|----|
| **场景** | **ODS 表现** | **五报送影响** |
| 主副卡 | 副卡一笔 + 主卡透支一笔 | EAST 两行都要；LVT 按主卡人归户判累计；1104 合计不能 double count |
| SWIFT 拆笔 | 本金 + 手续费 + 中间行扣费 | BOP 报本金；LVT 合并判阈值；EAST 逐笔明细；1104 费用进手续费收入 |
| 冲正/撤销 | 原借+原贷+红冲+蓝补 4 条 | LVT 冲正不报；BOP 超期要报更正；EAST 三行都要 |
| 钗汇分离 | 钗户/汇户分别入账 | BOP 申报金额取汇户折算；EAST 分钗/汇两行；1104 合并反映 |
| 资金池归集 | 子账户一笔 + 主账户归集一笔 | EAST 两行都报；BOP/LVT 按 event 归并；1104 只计主账户余额 |

**第三部分：交易类型映射规则管理架构**

用户（合规/业务岗）提供的“原始交易类型 + 字段组合 →
各监管交易类型”映射逻辑，需要结构化管理，避免散落在 SQL CASE WHEN 中。

**1. 四层架构**

|  |  |  |  |
|----|----|----|----|
| **层** | **载体** | **职责** | **谁维护** |
| 规则目录 | Collibra Business Term + Transformation Rule | 定义“为什么”（语义规则） | 合规岗 |
| 规则维表 | BQ reg_txn_mapping + reg_txn_mapping_target | 可执行（JOIN 用） | 数据工程师 |
| 规则执行 | Spark UDF / Dataform macro | DWD 消费维表，输出监管码 | 数据工程师 |
| 记录追溯 | reg_txn_mapping_lineage（自研） | 每笔交易命中哪条规则 | ETL 自动写 |

**2. reg_txn_mapping 维表设计**

> reg_txn_mapping（主表，渠道级）
>
> mapping_id PK
>
> channel -- CORE / NET_BANK / ATM / FOREX_SWIFT
>
> src_txn_type -- 原始交易类型码
>
> condition_json -- 字段组合条件（JSON）
>
> effective_from / effective_to
>
> rule_version -- 对应 Collibra Rule version
>
> created_by / approved_by
>
> reg_txn_mapping_target（多监管目标码，一对多）
>
> mapping_id FK
>
> reg_report -- YBT / EAST / BOP / LVT / 1104
>
> target_txn_code -- 各监管码
>
> target_label

**3. OpenLineage 的角色定位**

**OL 不负责**存映射逻辑，也不替 Collibra Rule。OL
的角色是“桥”：设计态（Collibra Rule）→ 实执行（OL Run 采到
rule_version + 维表 snapshot）→ 记录态（lineage 表这笔命中
mapping_id）。

OL Custom Facet 应
emit：rule_version、mapping_table_snapshot_dt、channel、src_txn_type、condition_match_cnt、各监管码分布。

**第四部分：GCP 技术栈部署建议**

基于 Google Cloud Platform 的统一数仓 + 治理工具链完整映射：

**1. 数据处理层**

|  |  |  |
|----|----|----|
| **工具** | **职责** | **监管场景** |
| Cloud Storage | 贴源 raw zone / 可信区归档 | ODS 落地 + 可信区 Bucket Lock |
| BigQuery | 数仓存储（ODS/DWD/DWS/ADS） | 五层表存储 + 规则维表 |
| Dataflow | Ingestion + PII 脱敏 + SWIFT 解析 | ODS 贴源、合规前置 |
| Dataproc | DWD 复杂归并（联名/SWIFT/冲正） | Spark UDF + OL Spark Plugin |
| Dataform | DWS/ADS SQL 建模 + Assertion | 总分核对 + 跨报送勾计 |
| Composer | 调度（托管 Airflow） | 五报送 DAG + DQ 阻断 |

**2. 治理层**

|  |  |  |
|----|----|----|
| **工具** | **职责** | **监管场景** |
| Collibra | Business Term + Transformation Rule | 字段级“应该是什么” |
| Dataplex | 技术目录 ↔ Collibra 双向 sync | GCP 资产统一管理 |
| Data Lineage API | 原生 OL 后端（替代 Marquez） | Run Event + LogicalPlan + Custom Facet |
| DQ Hub | 字段 DQ + 跨报送勾计 | 空/码值/总分核对/勾计 |
| DLP + KMS | PII 脱敏 + 加密 | 证件号/户名掩码 |
| VPC SC | 可信区隔离 | YBT/EAST/BOP 硬约束 |

**3. 报文/报送前置**

|  |  |  |
|----|----|----|
| **工具** | **职责** | **监管场景** |
| Cloud Run / GKE | 报文生成服务 | YBT 90 表 / BOP ASCII / EAST 定长 / LVT 人行格式 |
| Apigee | mTLS + 报文签名 + 重试 | 外管局/金监局前置机对接 |
| Pub/Sub | DQ 阻断 webhook | DQ FAIL → 阻断报文推送 |

**第五部分：迁移策略（三平台 → 统一平台 + YBT 新装）**

总策略：以 YBT 10 主题为 DWD 主干，EAST/BOP/LVT 往主干挂靠；EAST
走“一表通 2.1 → EAST 5.0”62 张表转换通道。

**Phase 0：主数据 + DIM 先统一**

主数据盘点：客户、账户、机构、产品、行业、国别、码值字典 ——
四套（EAST/BOP/LVT/YBT）对照

建统一 DIM（SCD2 拉链）：dim_cust / dim_acct / dim_org /
dim_dict_reg（行内码 → YBT → EAST → BOP 四向映射）

口径盘点表：EAST/LVT/BOP 三套老平台关键指标取数逻辑逐字段登记差异

**Phase 1：统一 DWD 主干**

按 YBT 10 主题建 DWD 业务过程表

三套老平台 ODS → DWD 映射一次做完，老 ODS 保留做回溯

YBT DWD = 主干本身

**Phase 2：DWS + 三老 ADS 并行双跑**

DWS 按监管主题建（信贷/资金/国际/同业），五报送共用

三老 ADS 在统一平台重建，从 DWD 按各监管字段映射

双跑比对 ≥ 2-3 个报送周期，差异率 \> 0.1% 阻断割接

**Phase 3：YBT 先割接 + EAST 走转换通道**

YBT 第一批割接（新平台 → 可信区 → 金监局）

EAST 走“YBT 2.1 → EAST 5.0”62 张表转换通道，不等同于直出 EAST

BOP/LVT 割接（不受 YBT 影响，双跑 OK 即切）

**第六部分：你可能没想到的问题（深水区预警）**

**1. 【逻辑断层】“无效/例外”规则的治理**

用户提供的映射逻辑常常只覆盖 80% 常规情况，剩下 20%
边缘场景靠开发人员“拍脑袋”写 ELSE，游离于 Collibra 之外。建议在
reg_txn_mapping 表中强制设立 Default/Fallback 规则，并标记
is_exception_flag，定期生成报表给合规部。

**2. 【时间陷阱】规则生效的“双时态”问题**

监管报表有强追溯性。必须区分：(a) 有效时间（业务上规则从哪天生效）；(b)
事务时间（数据实际进入系统的时间）。如果 1 月 1 日前的交易因 1 月 2
日重跑 DWD 错误应用新规则，即构成错报。DWD 层必须是 Immutable
历史快照，reg_txn_mapping 必须有 effective_start_date /
effective_end_date，Spark UDF 基于交易发生时间匹配当时有效规则版本。

**3. 【存储陷阱】BigQuery 的“时间旅行”与不可变性**

BQ 的 Time Travel 默认仅 7 天，远不够监管要求的 5 年追溯。严禁对 DWD
层使用 UPDATE/DELETE（除非数据修复且有审计）。对于超 7 天历史数据，依赖
Partition 不可变性，并定期将冷数据备份到 GCS 归档存储。

**4. 【合规死角】“非结构化”数据的血缘**

BOP 和 EAST 涉及 SWIFT MT/MX 报文、合同影像 OCR
结果等半结构化数据。建议在 Dataflow
阶段生成“解析元数据文件”（JSON），记录原始文件名、解析器版本、提取字段列表，并在
reg_record_lineage 表中记录 source_document_ref。

**5. 【流程断层】“紧急修正”的旁路**

监管报送有严格截止时间，发现数据错误时合规人员可能要求“先手工改 ADS
文件”。这种旁路操作会导致 OL 血缘断裂。建议明确定义 Break-glass
SOP：禁止直接修改 ADS 表；必须修改上游 reg_txn_mapping 或
ODS；如果时间来不及，允许在可信区通过脚本生成修正文件，但必须记录
manual_override_flag=True，下个周期在 DWD 彻底修复。

**6. 【资源黑洞】DWS 层的“派生指标”定义权**

1104 报表大量依赖派生指标（如“逾期 90 天以上贷款余额”）。DWS
层严禁定义新的业务口径，只能是 DWD
指标的聚合（SUM/COUNT）。所有业务口径（如“逾期”定义）必须沉淀在 DWD
层。Dataform 的 Assertion 不仅要核对总数，还要核对口径定义的一致性。

**第七部分：监管问询闭环链（示例）**

以“SWIFT UETR=abc123，CORE_RTGS_OUT，USD 10
万跨境同名转账”为例，展示四层追溯链路：

**第 1 层：Collibra（设计态）**

Rule TR_FX_OUT_CORP_SAME_NAME v2.3：

> IF channel=CORE AND src_txn_type=CORE_RTGS_OUT
>
> AND is_cross_border=Y AND counterparty_type=CORP AND same_name=Y
>
> THEN YBT=K02_03 / BOP=821990 / EAST=CROSS_OUT_CORP / 1104=境外资产

**第 2 层：reg_txn_mapping_lineage（记录态）**

> biz_event_no=ev_88271
>
> condition_snapshot={ccy:CNH, is_cross_border:Y,
> counterparty_type:CORP, same_name:Y}
>
> mapping_id=map_4721, rule_version=v2.3

**第 3 层：OpenLineage Run（运行态）**

> Dataproc app dwd_fx_daily @ 2025-03-15 02:14
>
> git commit a3f2c, rule_version=v2.3
>
> Custom Facet: mapping_table_snapshot_dt=2025-01-01
>
> Input: ods_forex_swift_di dt=20250315, 9281 rows
>
> Output: dwd_fx_payment_di, 9274 rows (7 笔冲正 filter)

**第 4 层：reg_record_lineage（记录级）**

> UETR=abc123 → biz_event_no=ev_88271
>
> → ADS_YBT: 一行 K02_03
>
> → ADS_BOP: 主申 821990 + (JW) 前缀
>
> → ADS_EAST: 一行 CROSS_OUT_CORP
>
> → ADS_1104: 境外资产栏含这笔

**四层拼齐，监管抽 20 笔能在 10 分钟内答完。**

**第八部分：各层一句话总结**

|  |  |  |  |
|----|----|----|----|
| **层** | **关键特征** | **输出** | **工具** |
| ODS | 贴源、按源系统分 schema | 可溯源原始数据 | Dataflow / BQ |
| DIM | SCD2、全行唯一、监管码映射 | 一致性维度 | Collibra + BQ |
| DWD | 按业务过程建业务表、币种保留、biz_event_no 归并 | 企业级标准明细（数出同源） | Dataproc + BQ |
| DWS | 按主题汇总（信贷/资金/国际） | 复用指标 + 质控基准 | Dataform / BQ |
| ADS | 按监管机构隔离、字段映射 + DQ | 各监管报送报文数据源 | Cloud Run + Apigee |

**核心铁律**

**1. 数出同源：**EAST / 一表通 / 1104 中同一笔贷款必须来自同一 DWD。

**2. SCD2 拉链：**客户行业/性质变更必须留历史。

**3. 可信区隔离：**ADS 产出 → 可信区 → 报送。

**4. 总分核对：**DWD SUM ↔ DWS ↔ 总账。

**5. 元数据文档：**每个监管字段的来源 DWD 字段 + 码值转换规则必须进
Collibra。

**6. 规则维表驱动：**业务改映射只改 reg_txn_mapping + 升 Collibra Rule
版本 → DWD 重跑即生效，5 个报送 SQL 一句不用改。

**文档生成时间：**2025 年（基于本 Session 全部对话内容整理）

**适用范围：**统一大数据平台（GCP）支撑 YBT / EAST / 1104 / BOP / LVT
五报送场景
