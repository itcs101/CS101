# Acceptance Criteria: <Story 名称>

> Jira：`KEY` | Requirement：`REQ-ID` | Test run：`RUN-ID`

## Business behavior

### AC-01 <名称>

- Given：<前置条件>
- When：<动作>
- Then：<可观察结果>
- Evidence：<链接/哈希>

## Regulatory and data controls

- [ ] 官方报表编号和版本正确
- [ ] 报送频率和截止时间正确
- [ ] 字段血缘可追溯
- [ ] 数据质量规则通过
- [ ] 数据驻留和跨境策略通过
- [ ] 无客户/交易原始数据进入 Jira、Git 或 AI 上下文

## Negative cases

| Case | Expected block or behavior | Result | Evidence |
| --- | --- | --- | --- |
| 缺少监管来源 | 阻止审批 | | |
| 缺少字段血缘 | 阻止发布 | | |
| 未授权生产操作 | Hook 阻止 | | |

## Sign-off

- QA：
- Business owner：
- Compliance owner：
- Release manager：
