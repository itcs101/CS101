# Skill Design: jira-requirement-review

## Purpose

检查 Jira Epic、Capability 和 Story 是否具备监管报送项目所需的结构化字段和验收条件。

## Trigger

创建或修改监管报送相关 Issue，或 Issue 尝试进入 `Compliance Review` 时触发。

## Checks

- 有父子关系和唯一 Jira Key。
- 关联 `intent.md`、`spec.md` 或批准的来源。
- 已填写 jurisdiction、regulator、L1-L5、报表编号和频率。
- 有数据驻留类别和控制负责人。
- Story 使用“作为角色，我想要能力，以便价值”。
- 验收标准可用 Given-When-Then 验证。
- 没有原始客户、交易或 Token 内容。

## Outputs

```text
PASS | WARN | BLOCK
字段：<field>
原因：<reason>
修复：<action>
```

## Human gate

Skill 只提出结果。业务负责人修复业务缺口，BA 修复结构缺口，合规负责人决定监管字段是否完整。

## Deterministic controls

将检查实现为 Jira Automation、CI 或 PR 校验。`BLOCK` 时禁止进入 `Compliance Review`，不能由 AI 自行覆盖。
