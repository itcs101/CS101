请你作为一名OWL本体工程师与提示词设计师，基于下面给出的合同管理原始需求，生成一个用于驱动大模型输出完整OWL本体定义的“提示词”（Prompt）。

要求（请把下面的内容直接当成要发送给大模型的提示词文本，不要在提示词里再包含多余的解释性文字）：

- 任务目标：生成一个完整、可落地、支持合同管理业务的OWL本体语义定义文件（优先以Turtle (`.ttl`) 格式输出，或在无法输出Turtle时输出RDF/XML），并将文件保存为 `contract_ontology.ttl`（或给出相应可替换的文件名）。
- 输出风格：只输出本体文件内容（即OWL文件的文本），不要输出额外的分析、说明或元信息；在本体中须包含中文的 `rdfs:label` 与 `rdfs:comment` 注释来解释术语。

输入的业务要点（请将这些要点视作建模需求）：

1) 合同信息录入：在录入合同基本信息时需要同时录入合同条款（Clause）信息，条款可能有类型（如价格条款、服务条款、验收条款等）。
2) 合同开票信息录入：记录开票时间、开票金额、税率、发票号、发票状态等关键字段，发票必须关联到特定合同或合同项（contract item）。
3) 合同收款信息录入：收款记录应能关联到具体合同与相关发票，包含收款时间、金额、收款方式、收款账户等。
4) 合同查询：支持基于合同编号、合同名称、产品线、部门、时间等字段的模糊查询；查询结果可点击进入合同详细信息视图。

模型构建要求（必须包含且尽量详尽）：

- 本体头部：定义清晰的Base IRI（例如 `http://example.org/contract#`），并声明常用前缀（rdf,rdfs,owl,xsd,prov等）。
- 核心类（Classes）：明确至少包含 `Contract`、`ContractClause`、`Invoice`、`Payment`、`Party`（及 `Person`/`Organization` 子类）、`ProductLine`、`Department`、`ContractItem`（可选）、`Currency`、`TaxRate` 等。为每个类提供中文 `rdfs:label` 与 `rdfs:comment`。
- 类层次（Subclassing）：若适用，定义子类关系（例如 `Invoice` 的子类 `VATInvoice`、`ElectronicInvoice` 等；`Party` 的子类 `Supplier`、`Customer`）。
- 对象属性（ObjectProperties）：定义关键关系并给出域和余域（domain & range），例如 `hasClause`、`issuedInvoice`、`hasPayment`、`relatedToProductLine`、`belongsToDepartment`、`hasParty`、`hasContractItem`、`referencesContract` 等。为每个属性提供中文注释。
- 数据属性（DataProperties）：定义合同编号（contractNumber）、合同名称（contractName）、签署日期（signedDate）、生效日期（effectiveDate）、结束日期（endDate）、金额（amount）、发票号（invoiceNumber）、税率（taxRate）、金额币种（currencyCode）等数据属性并指定合适的XSD类型与约束（如 `xsd:date`、`xsd:decimal`、`xsd:string`）。
- 约束与公理：使用OWL断言（如最小/最大基数限制、必要条件/充分条件）描述关键约束，例如：
  - 每个 `Contract` 应至少关联一个 `Party`（签约方）和至少一个 `ContractClause`；
  - `Invoice` 必须引用一个 `Contract`（或 `ContractItem`）；
  - `Payment` 应能关联到 `Invoice` 或直接关联到 `Contract`；
  - 对金额字段使用 `xsd:decimal` 并注明币种（`Currency`或 `currencyCode`）。
- 规则与推理（SWRL 或规则注释）：给出若干示例规则以支持业务逻辑推断，例如：
  - 若 `Payment` 的 `paidAmount` 等于 `Invoice` 的 `invoiceAmount` 且 `invoiceStatus` 为已开票，则将 `Invoice` 标记为已结清；
  - 若 `Invoice.issueDate` 在 `Contract.signDate` 之前，则标记为异常（示例规则）；
  - 支持将 `Payment` 自动关联最近的未结算 `Invoice`（提供可用的SWRL或伪规则）。
- 示例实例（Individuals）：创建至少 3 个示例实例，覆盖 `Contract`、`ContractClause`、`Invoice`、`Payment`、`Party` 等，示例数据应使用真实样式的字段值（如合同编号 `CN-2026-0001`、金额 `100000.00`、税率 `0.13`、日期格式 `2026-01-01`），以便直接被系统或示例查询使用。
- 注释与文档化：为主要类/属性添加详细中文注释，给出可选的SPARQL查询例子（作为注释），用于展示如何按合同编号、合同名称、产品线、部门、时间区间进行查询（注释内展示，不作为运行输出）。
- 输出格式：优先以Turtle（`.ttl`）格式完整输出OWL本体文本，保证可被常见的本体编辑器（如Protege）或RDF库直接加载；若输出为RDF/XML，请确保语法与名称空间完整。

交付要求（当大模型执行本提示词时应满足）：

1. 直接输出OWL文件内容（Turtle或RDF/XML），不要额外包裹解释文字；
2. 本体应包含前缀、ontology注释、所有类/属性/实例定义与注释；
3. 包括至少 3 条可执行的SWRL规则或明确的伪规则注释；
4. 包含示例个体和至少两个注释中的SPARQL查询示例；
5. 指明建议的文件路径 `newdoc/contract_ontology.ttl`（作为保存目标）。

额外指令（可选但推荐）：

- 在本体中使用清晰的命名约定（驼峰或下划线）并在注释中说明所用命名约定；
- 若有必要，用 `owl:deprecated` 标注不建议使用的类/属性；
- 如需扩展，请在本体末尾留下注释段落，列出未来可能需要的扩展点（例如：电子签名、合同履约里程碑、违约赔偿、审批流程等）。

请将以上内容构造成一个高质量的、可直接发送给大模型（如OpenAI系列或本地Llama变体）的提示词文本，并把最终提示词写入当前文件（本文件即 `sample.md`）。

注意：本文件只应包含该用于生成OWL本体的提示词文本本身（即上面所述的Prompt），不要再包含我方的工作流程说明或其它多余说明。
