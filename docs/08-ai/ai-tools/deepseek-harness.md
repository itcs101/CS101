---
title: DeepSeek Harness
---

# DeepSeek Harness

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 是 DeepSeek 开源的 Agent 运行时与工具编排框架。它的目标不是只提供一个模型接口，而是把模型、工具、Skill、上下文、文件和执行环境组织成一个可扩展的 Agent 系统。

## 核心概念

DeepSeek Harness 可以理解为连接模型与执行环境的“骨架”或运行时，主要负责：

- 组装系统提示词和运行时上下文
- 管理 Agent 可使用的 Skill
- 提供 Shell、子进程和代码运行能力的抽象接口
- 管理附件、文件路径和本地工作区
- 将模型请求转换为工具调用，并把结果返回给模型继续推理

项目在 npm 上提供了多个 `@deepseek-ai/dsh-*` 包。例如，`dsh-system-prompt` 负责系统提示词组装，`dsh-skill` 负责 Skill 提供者注册，`dsh-shell` 和 `dsh-code-runtime` 则分别抽象 Shell 与代码执行能力。

## 适合什么场景

- 构建需要调用工具的代码 Agent
- 将 Skill、文件系统和命令执行能力接入模型
- 设计可替换的 Shell、代码运行时或附件存储实现
- 在本地或服务端搭建长程 Agent 的执行循环
- 将模型层与具体操作系统、沙箱或企业工具解耦

## 为什么需要 Harness

模型本身只能生成文本或工具调用意图。真正完成任务还需要一层运行时来处理权限、参数验证、工具执行、结果回传、上下文更新和错误恢复。Harness 将这些职责集中起来，使 Agent 的执行过程更容易扩展、测试和替换。

一个典型执行链路如下：

1. 用户提交任务。
2. Harness 组装系统提示词、Skill 和当前上下文。
3. 模型返回文本或工具调用。
4. Harness 校验参数并检查工具权限。
5. 运行 Shell、代码或其他工具。
6. 将工具结果写回对话上下文。
7. 模型根据结果继续推理，直到任务完成。

## 使用时的注意事项

Harness 暴露了 Shell 和代码执行等高权限能力，部署时不应默认授予 Agent 完整的主机权限。实际应用应至少配置：

- 工具白名单和最小权限
- 命令执行沙箱
- 网络访问限制
- 文件系统访问边界
- 超时、并发和资源配额
- 工具调用日志与审计记录

## 相关链接

- [GitHub 仓库](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek AI npm packages](https://www.npmjs.com/org/deepseek-ai)
- [DeepSeek Harness system-prompt package](https://www.npmjs.com/package/@deepseek-ai/dsh-system-prompt)
