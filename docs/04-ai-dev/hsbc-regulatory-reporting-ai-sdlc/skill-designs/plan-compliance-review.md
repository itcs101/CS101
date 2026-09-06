# Skill Design: plan-compliance-review

## Purpose

在实现前检查 `plan.md` 是否覆盖批准的规范、监管控制、测试证据和回滚路径。

## Trigger

`plan.md` 创建、修改或 PR 创建时触发。

## Checks

| Area | Required evidence |
| --- | --- |
| Scope | 每个 Spec requirement 有实现位置 |
| Regulatory | L1-L5、报表版本和复审日期已关联 |
| Data | 驻留、跨境、日志、备份和模型边界已说明 |
| Testing | 每项关键控制有可重复的测试 |
| Security | 敏感路径、凭据和生产权限有保护 |
| Operations | 监控、回滚、重算和人工放行已定义 |
| Audit | Jira Key、commit SHA 和证据位置完整 |

## Outputs

- `PASS`：可以进入实现
- `REVISE`：列出缺口和负责人
- `BLOCK`：存在未批准的高风险设计

## Human gate

工程师确认技术可行性；架构师确认方案；合规、数据保护和发布负责人按风险等级审批。AI 不得将 `REVISE` 或 `BLOCK` 改成通过。

## Deterministic controls

PR 检查工件字段、计划与 Story 的关联、测试命令和回滚证据。生产变更仍需发布经理授权。
