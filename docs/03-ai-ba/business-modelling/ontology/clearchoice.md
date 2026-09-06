# 银行监管报送（1104、EAST、金融基础数据、人行大集中、XBRL财报）本体建模工具分级推荐

**选型原则**：监管本体核心诉求=**监管指标语义建模+报表口径映射+数据血缘绑定+规则推理校验+制度版本管理+对接报送ETL**，分**科研/初稿建模、行内落地商用、开源自研全链路、代码自动化批量建本体**四大类，适配国内银行监管场景。

## 一、初稿&业务专家建模首选：Protégé（全银行通用、免费首选）

1. **适用场景**：业务+监管专家梳理1104指标本体、EAST明细项概念、监管制度术语本体、FIBO金融本体本地化改造、监管口径词典建模。
2. **监管关键能力**
   - 原生OWL2/RDF/Turtle，导入Excel/CSV批量生成监管指标类、属性；
   - 预装HermiT推理机：自动校验**指标口径冲突、字段重复、勾稽逻辑矛盾**（1104表内/表间校验本体一致性）；
   - 插件：SHACL校验、SPARQL查询、XBRL导入插件（适配财报报送XBRL规范）、SKOS叙词表（监管代码字典本体）；
   - WebProtégé网页版：多部门（计财、风控、报送、IT）在线协同编辑监管本体、版本留痕。
3. **优缺点**
   ✅零费用、中文友好、国内银行监管本体项目90%初稿均用；
   ❌无原生数据血缘、无法直接对接生产库与报送ETL，仅做概念建模。

## 二、大中型银行投产级商用本体（落地1104+EAST生产本体，首选TopBraid/Regnology）

### 1、TopBraid Composer（国际金融监管本体标杆，外资+头部股份制标配）

- **监管独有优势**：
  1. 原生**XBRL→OWL自动转换**，直接导入财报、1104报表XML规范生成监管本体（欧美FRO监管本体、FIBO本体原生基于TBC开发）；
  2. 内置SPARQL+SHACL双校验，把EAST校验规则、1104勾稽关系写成本体约束，自动校验报送数据合规；
  3. 本体可直接导出映射脚本，对接数据仓库、报送平台ETL，实现**源系统字段→监管指标本体→报送报表全链路映射**；
  4. 版本管控：监管制度改版（如EAST5.0升级）本体分支管理、变更影响自动分析。
- **适配**：国有大行、股份制行做全行统一监管语义底座。

### 2、Regnology Metadata Modeller（全球监管报送专用本体工具，监管机构御用）

- 专为**监管DPM（Data Point Model数据点模型）**设计，完美匹配国内1104/EAST细粒度数据点建模；
- 业务监管人员低代码拖拽建模，自动拆分监管条文→指标→明细字段三层本体，内置EBA/ECB监管本体标准，国内城商行、农商行落地监管报送首选商用。

### 3、OntoStudio（西门子，工业+金融双场景）

擅长**异构数据源本体融合**：核心账务、信贷、资金、理财多源系统字段对齐EAST/1104监管本体，适合集团银行多子行监管口径统一。

## 三、国内银行国产化落地：监管报送+元数据一体化平台（本体+血缘+报送三合一）

> 国内银行很少纯OWL本体落地，主流**元数据平台内嵌本体建模**，本体直接绑定报送数据血缘、口径、校验规则

### 1、亿信睿治（亿信华辰，国内监管报送龙头）

- 内置**1104/G报表、EAST全指标预置本体模型**，开箱即用；
- 可视化本体建模：业务人员拖拽维护监管指标语义、口径定义，自动生成从源表到报送报表的血缘本体；
- 本体约束直接转化为报送校验规则，一键生成1104/EAST校验脚本，城商行、农商行落地首选。

### 2、Apache Atlas（开源元数据底座，自研监管本体首选）

- 免费开源，**分类体系=轻量化本体**，自定义监管分类：1104分类、EAST主题域、产品本体；
- Hook采集数仓、ODS源系统元数据，建立**物理字段→监管指标本体映射关系**，自动计算报送变更影响；
- 适合大行自研监管治理平台，搭配Neo4j存储本体关系。

### 3、Aloudata大应主动元数据

主动式本体建模，数据源变更自动更新监管指标本体，制度改动自动预警受影响报送报表（1104/EAST变更影响分析刚需）。

## 四、代码自动化批量建本体（海量EAST明细、十万级监管指标批量生成）

### Python栈（中小银行自研）

1. **owlready2+rdflib**：读取报送元数据字典、1104指标文档，代码批量生成OWL监管本体，导出Turtle对接图数据库；
2. PySHACL：批量编写EAST校验本体约束。

### Java栈（大行）

1. **OWLAPI**：Protégé底层内核，对接数据字典接口自动化生成监管本体；
2. Apache Jena：RDF本体存储+SPARQL引擎，本体服务化提供指标口径查询。

## 五、图数据库配套本体（本体落地查询、报送校验）

1. **Stardog**：RDF原生库，本体+实例一体化，导入1104本体+报送数据，SPARQL校验报表合规；
2. **Neo4j+Neosemantics**：图数据库挂载RDF本体，把EAST明细数据导入图，基于本体做穿透式合规检查（贷款五级分类、不良迁徙校验）。

## 六、分银行规模落地选型速查表

| 银行类型      | 本体建模主工具     | 辅助工具          | 核心用途                                       |
| ------------- | ------------------ | ----------------- | ---------------------------------------------- |
| 国有/股份制   | TopBraid+亿信睿治  | Protégé+Stardog | 全行统一监管语义、1104+EAST+财报全品类报送本体 |
| 城商行/农商行 | Regnology/亿信睿治 | Protégé         | 监管指标落地、快速响应监管制度更新             |
| 小型村镇行    | Protégé+Excel    | owlready2         | 轻量化监管术语、简易1104本体                   |
| 自研技术团队  | Apache Atlas+Jena  | TopBraid试用版    | 自主搭建监管本体治理平台                       |

## 补充：FIBO金融行业标准本体配套

银行做监管报送建议先导入**FIBO开源金融本体（存贷、同业、资本、理财）**，再在其上扩展国内1104/EAST本地化监管子类，TopBraid/Protégé均支持一键导入FIBO官方OWL包。

> [FIBO官方文档](https://www.fibo.org/documentation/fibo-documentation/)
> [FIBO官方OWL包](https://www.fibo.org/downloads/fibo-owl-packages/)
> [FIBO官方RDF包](https://www.fibo.org/downloads/fibo-rdf-packages/)
> [Exploring FIBO Using the Inference and Property Path Features of GraphDB](https://www.ontotext.com/blog/fibo-graphdb-inference-and-property-path-features/)
> [FIBO github](https://github.com/edmcouncil/fibo)

### Protégé一键全量导入FIBO官方OWL（银行监管报送专用，2种一键方案）

**前提：Protégé 5.2及以上版本（推荐5.5/5.6），提前装好HermiT/ELK推理机插件**
FIBO分**正式生产版Production（季度稳定版，银行建模首选）、开发版Development（实时更新草稿）**，官方一键入口靠 `LoadFIBO.rdf`总入口自动递归拉取全部分包本体（BE/SEC/IND/Derivatives等全部金融模块）。

#### 方案一：在线一键远程导入（最省事、实时最新FIBO，推荐监管建模）

##### 1、打开Protégé，新建空白OWL本体（File→New ontology，自定义IRI随便填，如 `http://bank-reg/fibo-local`）

##### 2、顶部菜单：`File → Open from URL`（快捷键 Win：`Ctrl+Shift+O` Mac：`Cmd+Shift+O`）

粘贴对应链接，**一键加载全量FIBO所有OWL依赖包**：

- ✅【银行监管必选·正式生产版】（稳定、经过校验，适配1104/EAST映射）
  `https://spec.edmcouncil.org/fibo/ontology/master/latest/LoadFIBOProd.rdf`
- 开发测试版（前沿新规范，不建议生产本体）
  `https://spec.edmcouncil.org/fibo/ontology/master/latest/LoadFIBODev.rdf`

##### 3、点击OK，等待自动下载

Protégé自动递归解析所有 `owl:imports`依赖，**一次性载入BE主体实体、SEC证券、IND存贷款、Deriv衍生品、FBC财务合约全模块OWL**，全程无需逐个下载子文件。

> 加载耗时：1～5分钟（看网速，全FIBO约3万+金融类）

##### 4、加载完成保存本体

File→Save As，保存为 `.owl`本地文件，后续打开不用重复联网下载。

#### 方案二：离线一键导入（内网银行无外网环境，本地全量包）

##### 步骤1：下载FIBO QuickStart离线大包（单文件全集Turtle）

官方QuickStart整合全部FIBO内容，单 `.ttl`文件，不用拆分多OWL：
生产版：https://spec.edmcouncil.org/fibo/ontology/master/latest/prod/quickstart/fibo-quickstart-prod.ttl
开发版：https://spec.edmcouncil.org/fibo/ontology/master/latest/dev/quickstart/fibo-quickstart-dev.ttl

##### 步骤2：Protégé→File→Open，选中下载的 `fibo-quickstart-prod.ttl`，直接打开即全量导入FIBO。

#### 方案三：只导入FIBO局部模块（银行监管常用：仅主体+存贷，精简加载）

不用全量，按需导入单个模块总入口：

1. 主体实体BE（开户、法人、机构，1104法人监管）：
   `https://spec.edmcouncil.org/fibo/ontology/BE/LoadBE.rdf`
2. 存贷款IND（信贷、对公/零售贷款，EAST信贷明细）：
   `https://spec.edmcouncil.org/fibo/ontology/IND/LoadIND.rdf`
   打开方式同上：`Open from URL`粘贴链接一键载入单模块。

### 银行监管落地优化&避坑（1104/EAST建模必备）

1. **加载后切换推理机：菜单栏Reasoner→HermiT Reasoner→Start reasoner**，自动推理FIBO父子类关系，用于监管指标口径对齐校验。
2. **网络加载慢/超时解决方案**
   修改Protégé启动参数：编辑 `run.bat/run.sh`，JVM参数添加：
   `-Djava.util.Arrays.useLegacyMergeSort=true`，解决FIBO大本体加载报错。
3. **后续自建监管本体引用FIBO**
   你的1104/EAST本体：File→Import ontology→From URL，填入上面LoadFIBOProd地址，**引用而非复制FIBO本体**，减少文件体积、方便后续FIBO版本升级。
4. 国内网络访问慢：先用浏览器下载 `LoadFIBOProd.rdf`本地，再Open本地rdf文件，Protégé仍会自动在线拉取剩余子OWL。

### 落地建议（银行监管报送）

- 正式监管指标建模：**LoadFIBOProd生产版全量导入**
- 信贷EAST专项建模：只导入BE+IND两个模块
- 内网隔离环境：使用QuickStart离线ttl大包
