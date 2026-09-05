# Skill Design: regulatory-intake

## Purpose

将受控的监管来源、内部问询或生产事件整理为可审查的 `intent.md`，不做最终法律解释。

## Trigger

当用户提供新的监管文件 ID、报表模板版本、监管问询、控制带异常或监管规则变更时触发。

## Inputs

- 受控来源链接或文档 ID
- 市场、监管机构和适用日期
- 事件或问题的脱敏描述
- 相关 Jira Key（如已有）

## Procedure

1. 读取来源的元数据和允许处理的内容。
2. 提取适用范围、报表编号、频率、截止时间和待确认事项。
3. 标出 L1-L5 分类和数据驻留问题；不确定项标记 `Pending`。
4. 生成 `templates/intent.md` 的副本。
5. 检查是否包含客户、交易、账号、Token 或原始载荷；发现则停止并删除敏感内容。

## Outputs

- `intent.md`
- 影响范围摘要
- 未决问题清单
- 需要合规确认的判断列表

## Human gate

产品负责人确认问题和结果；监管合规负责人确认来源、jurisdiction 和解释范围后，才能进入 `spec.md`。

## Deterministic controls

CI 检查必填元数据、敏感信息模式、来源链接和 Jira Key。Skill 不得自行批准需求。
