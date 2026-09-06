---
title: CodeGraph
---

# CodeGraph

[CodeGraph MCP](https://www.npmjs.com/package/@astudioplus/codegraph-mcp) 是面向代码库理解的 MCP Server。它把代码解析、符号关系和跨文件依赖整理成 Agent 可以查询的结构化信息，帮助模型从“搜索文本”进一步走向“理解代码关系”。

## 它解决什么问题

传统的关键词搜索适合找文件和字符串，但不容易回答以下问题：

- 一个函数被哪些模块调用？
- 某个类实现了哪些接口？
- 修改一个类型会影响哪些文件？
- 某个 API 从入口到数据库的调用路径是什么？
- 一个模块与其他模块之间有哪些依赖关系？

CodeGraph 将这些关系组织成代码图谱，再通过 MCP 暴露给支持 MCP 的 AI 客户端或 Agent。

## CodeGraph、Graphify 与 GitNexus

这三个工具都可以帮助 Agent 理解项目，但关注点并不相同。这里的 Graphify 指 [@sentropic/graphify](https://github.com/rhanka/graphify)，而不是 npm 中其他同名的随机图生成或数据分析包。

| 工具 | 主要对象 | 主要入口 | 更适合的场景 |
| --- | --- | --- | --- |
| **CodeGraph MCP** | 多语言代码库、符号、定义、引用和依赖 | MCP Server | 让 VS Code、Copilot 或其他 MCP Agent 查询代码关系 |
| **Graphify** | 代码、文档、论文、图片和音视频转录等混合资料 | Agent Skill、CLI 或 MCP 生态 | 把项目代码和知识资料一起建成可查询知识图谱 |
| **GitNexus** | Git 仓库中的代码结构、调用链、执行流和影响范围 | CLI、MCP Server 和本地索引 | 代码导航、变更影响分析、调用链追踪和 Agent 代码理解 |

### 能力侧重点

**CodeGraph MCP** 更像一个代码关系查询服务。它强调跨语言解析、符号关系和 MCP 工具集成，适合在 Agent 工作过程中按需查询定义、引用、调用方、被调用方和影响范围。

**Graphify** 更像一个通用知识图谱构建与查询 Skill。它的输入不只限于源代码，也可以包含设计文档、论文、图片和音视频转录。适合回答“代码实现与项目资料之间有什么关系”这类跨资料问题，但代码级调用链的准确性和深度应以实际解析器与配置为准。

**GitNexus** 更强调 Git 仓库内的代码智能。它适合围绕代码变更进行导航、调用链分析、执行流理解和影响范围判断，尤其适合在修改前评估 blast radius，在修改后让 Agent 回看相关路径。

### 简单选型

- 主要需求是 **通过 MCP 查询代码符号和依赖**：优先考虑 CodeGraph MCP。
- 需要把 **代码、Markdown、设计文档和其他资料放在同一知识图谱中查询**：考虑 Graphify。
- 主要工作是 **理解 Git 仓库、调用链和修改影响范围**：考虑 GitNexus。
- 需要同时满足代码关系和项目资料检索：可以组合使用，但应明确每个工具的索引范围，避免重复索引和结果冲突。

### 对比时应验证的指标

工具名称和宣传功能不能代替实际验证。选择前建议在同一个小型仓库上比较：

1. 支持的语言、框架和构建系统。
2. 定义、引用、调用链和继承关系的准确率。
3. 增量索引和分支切换后的更新速度。
4. 大型仓库的索引时间、内存和磁盘占用。
5. MCP 工具数量、返回结果结构和 Agent 易用性。
6. 对动态调用、反射、代码生成和测试文件的处理方式。
7. 私有代码是否可以完全本地运行，网络访问和数据上传边界是什么。

不同版本的工具能力会变化，实际支持的语言、工具数量和命令参数应以对应仓库或 npm 包的当前文档为准。

## 主要能力

根据公开包说明，CodeGraph MCP 面向多语言代码智能场景，提供包括以下方向的能力：

- 代码库索引与结构分析
- 文件、符号、类、函数和接口查询
- 定义、引用、调用方和被调用方分析
- 跨文件依赖关系探索
- 面向 Agent 的代码问答工具
- 通过 MCP 接入 VS Code、Copilot 或其他 Agent 客户端

实际可用的工具数量和支持语言以当前版本文档为准。使用前应先确认项目的解析器覆盖范围，以及大型代码库建立索引所需的时间和存储空间。

## 典型使用方式

1. 在目标代码库中启动或配置 CodeGraph MCP Server。
2. 让服务器扫描项目文件并建立索引。
3. 在 MCP 客户端中注册该 Server。
4. 通过自然语言提出代码关系问题。
5. Agent 调用图谱工具，结合返回的定义、引用和依赖继续分析。

例如，可以让 Agent 回答“解释用户登录请求从路由到持久化层的调用链”，也可以在修改前查询“这个公共接口有哪些调用方”。

## 与普通代码搜索的区别

普通搜索主要返回包含关键词的文本行；CodeGraph 更关注代码元素之间的语义关系。二者适合配合使用：搜索用于快速定位文本和配置，CodeGraph 用于理解定义、引用、调用链和影响范围。

CodeGraph 不能替代编译器、测试和人工审查。图谱查询结果依赖解析器、构建配置和索引状态；动态语言、反射、代码生成和运行时依赖可能导致静态关系不完整。

## 使用建议

- 先为核心仓库建立索引，再逐步扩大范围。
- 将图谱查询和普通文本搜索结合起来。
- 修改代码前先查询影响范围，修改后运行编译和测试。
- 不要把未审查的图谱结果直接当作业务事实。
- 对私有代码库控制 MCP Server 的文件和网络权限。

## 相关链接

- [CodeGraph MCP npm 包](https://www.npmjs.com/package/@astudioplus/codegraph-mcp)
- [CodeGraph GitHub 仓库](https://github.com/codegraph-ai/CodeGraph)
- [Graphify GitHub 仓库](https://github.com/rhanka/graphify)
- [Graphify npm 包](https://www.npmjs.com/package/@sentropic/graphify)
- [GitNexus GitHub 仓库](https://github.com/abhigyanpatwari/GitNexus)
- [GitNexus npm 包](https://www.npmjs.com/package/gitnexus)
- [MCP 官方文档](https://modelcontextprotocol.io/)
