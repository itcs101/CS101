# 02 Jira 流转与 Source of Truth

## 1. 双系统职责

| 内容 | 权威系统 | Jira 中保存 | Git 中保存 |
| --- | --- | --- | --- |
| 工作项状态、负责人、优先级、Sprint | Jira | 完整值 | 可选快照 |
| 工件正文和版本 | Git | 路径与 commit SHA | 完整正文 |
| 审批决定 | Jira + PR | 审批人、时间、决定 | PR 记录与引用 |
| 原始客户/交易数据 | 属地数据系统 | 禁止写入 | 禁止写入 |
| 测试和运行证据 | 受控证据库 | 链接、哈希、结果 | 摘要和链接 |

冲突处理：Jira 决定工作状态和审批状态，Git 决定工件正文；若两者的 Key、SHA 或状态不一致，流程自动进入 `Blocked`，由项目管理员处理。

## 2. Issue 层级

```text
Regulatory Requirement
  └── Epic: 报表族或监管能力
        └── Capability/Feature: 业务或技术能力
              └── Story: 可验收的需求
                    └── Task/Sub-task: 实施、测试、证据和发布工作
```

使用 Jira `is child of` 或组织已批准的等价关系，禁止只用标题文本表达父子关系。

## 3. 推荐工作流

`Draft → Analysis → Compliance Review → Approved → In Progress → Testing → Review → Release Approval → Done`

异常状态：`Blocked`、`Rejected`、`Deferred`、`Rolled Back`。

状态进入条件：

- `Analysis`：已有 `intent.md` 和监管来源记录。
- `Compliance Review`：`spec.md` 完成，L1-L5、jurisdiction、报表编号、数据分类和未决问题已填写。
- `Approved`：产品、合规和架构责任人完成审批。
- `Testing`：实现与 `plan.md` 建立关联，并提交自动化测试结果。
- `Release Approval`：PR 已通过检查、追溯矩阵完整、回滚方案已演练。
- `Done`：发布记录、证据哈希和 Jira/Git 关联已归档。

## 4. Jira 必填字段

| 字段 | 说明 |
| --- | --- |
| `Regulatory source ID` | 官方文件或内部受控来源的 ID，不填原文敏感内容 |
| `Jurisdiction` | 市场/司法辖区 |
| `Regulator` | 监管机构 |
| `L1-L5 classification` | 监管大类、子类、机构、报表标识、频率 |
| `Data residency class` | 强制本地存储 / 本地副本 / 自由流转 / 待确认 |
| `Artifact path` | Git 中工件路径 |
| `Artifact commit SHA` | 已审批版本的提交 SHA |
| `Risk level` | R1-R4 |
| `Control owner` | 合规、数据保护、安全或架构负责人 |
| `Evidence link` | 测试、审批或运行证据链接 |
| `Review due date` | 规则复审日期 |

## 5. Jira 与 Git 的最小同步规则

1. 创建 Jira Issue 时生成或关联唯一 `REQ-*` 或 `CHG-*` 标识。
2. 工件 front matter 或顶部元数据写入 Jira Key。
3. Jira 进入 `Approved` 前必须存在对应 commit SHA。
4. PR 必须引用 Jira Key，并自动检查工件 SHA 是否仍为最新审批版本。
5. 合并后将 PR、测试结果、发布版本和证据哈希回写 Jira。

## 6. 权限

Jira 按角色限制字段编辑；合规字段只能由合规责任人修改，发布审批只能由发布经理或其授权代理完成。AI 身份不得拥有生产发布审批权限，也不得绕过分支保护。
