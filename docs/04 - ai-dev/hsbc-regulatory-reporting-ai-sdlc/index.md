# 汇丰监管报送 AI 原生 SDLC

本目录将 [AI 原生 SDLC 手册](../ai-native-sdlc-playbook.md) 转化为面向汇丰银行监管报送类项目的实施方案。方案采用 Jira 驱动工作流、Git 版本化工件和人工审批门，首版面向跨市场通用场景，不替代任何市场的法律或合规判断。

## 阅读顺序

1. [实施方案](01-实施方案.md)
2. [Jira 流转与权威数据源](02-jira流转与source-of-truth.md)
3. [工件链与监管追溯](03-工件链与监管追溯.md)
4. [领域约束与控制点](04-领域约束与控制点.md)
5. [Skill 策略与推荐清单](05-skill策略与推荐清单.md)
6. [实施路线图与验收指标](06-实施路线图与验收指标.md)

## 模板

- [Intent 模板](templates/intent.md)
- [Spec 模板](templates/spec.md)
- [Plan 模板](templates/plan.md)
- [Jira Epic 模板](templates/jira-epic.md)
- [Jira User Story 模板](templates/jira-user-story.md)
- [验收标准模板](templates/acceptance-criteria.md)
- [监管追溯矩阵模板](templates/traceability-matrix.md)
- [评审记录模板](templates/review.md)
- [变更记录模板](templates/change-record.md)

## Skill 设计稿

- [监管需求摄取](skill-designs/regulatory-intake.md)
- [Jira 需求检查](skill-designs/jira-requirement-review.md)
- [数据属地化检查](skill-designs/regulatory-data-localization-review.md)
- [报送血缘检查](skill-designs/reporting-lineage-review.md)
- [计划合规检查](skill-designs/plan-compliance-review.md)

## 重要边界

- Jira 只保存工作项元数据、状态和审批记录，不保存客户、交易或原始监管报送数据。
- Git 只保存脱敏后的工件、规则元数据和证据链接；原始数据留在受控的属地系统。
- Skill 负责分析和提出建议；必须强制执行的控制由 Hook、CI、PR 分支保护和人工审批实现。
- 监管要求、数据出境、留存期限和模型部署区域必须由对应的合规或安全负责人确认。
