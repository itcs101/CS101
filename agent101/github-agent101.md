# GitHub Copilot 使用指南

> 基于 VS Code 官方 GitHub Copilot 文档整理，重点覆盖 Concepts、Agents、Chat、Customization 与 Best Practices。

## 一、先建立正确心智模型

> 在 VS Code 里，Copilot 不是单一功能，而是一组从“轻量补全”到“端到端执行”的连续能力：

|                    |                                              |                                      |                                |
| :----------------: | :------------------------------------------: | :-----------------------------------: | :-----------------------------: |
|   **能力**   |                **作用**                |          **适合场景**          |       **典型入口**       |
| Inline Suggestions |           边写边补全、生成局部代码           |       写函数、补样板、填变量名       |        编辑器内直接触发        |
|    Inline Chat    |             在当前文件就地改代码             |     小范围重构、加校验、解释代码     |             Ctrl+I             |
|     Chat / Ask     |         多轮问答、理解代码、补上下文         |       问架构、问设计、定位问题       |           Ctrl+Alt+I           |
|        Plan        |                 先规划再执行                 |      多文件需求、迁移、复杂重构      |     Chat 中切到 Plan agent     |
|       Agent       | 理解目标、拆步骤、改多文件、跑命令、验证结果 |      端到端实现、调试、批量修改      | Chat Agent 模式或 Agents window |
|   Smart Actions   |                一键式 AI 动作                | 生成 commit message、修复错误、重命名 |      命令面板 / 上下文菜单      |

> **最重要的判断标准：**如果任务只影响当前代码片段，用 Inline Suggestions 或 Inline Chat；如果任务跨文件且需要自己执行、验证、修复，就该用 Agent；如果需求复杂但你还不想马上改代码，先用 Plan。

**官方总览：**[<u>GitHub Copilot in VS Code</u>](https://code.visualstudio.com/docs/copilot/overview)

## 二、最快上手路径

1. 先在状态栏完成 **Set up Copilot**。
2. 打开 Chat：Ctrl+Alt+I。
3. 从一个明确任务开始，而不是“试试看 AI 能做什么”。
4. 对当前仓库执行一次 /init，生成项目级 AI 指令。
5. 学会 4 个最常用动作：#file / \#codebase / /compact / /fork。

**一个适合第一次体验的 Prompt：**

Create a basic Node.js web app for sharing recipes. Make it look modern and responsive.

## 三、Concepts：理解 Copilot 真正是怎么工作的

### 1. Language Models

> **作用：**语言模型决定 Copilot 的推理风格、速度、代码质量和成本。官方文档明确建议根据任务复杂度切换模型，而不是始终用同一个模型。

**配置位置：**

- Chat 输入框里的 **model picker**：切换 Chat / 编辑类请求的模型。
- **Chat: Manage Language Models**：管理可见模型、固定常用模型、添加 BYOK 模型。
- inlineChat.defaultModel：Inline Chat 默认模型。
- chat.utilityModel / chat.utilitySmallModel：utility tasks 使用的模型。
- chatLanguageModels.json：BYOK provider 或 custom endpoint 详细配置。

> **怎么用：**简单补全和样板代码用更快的模型；设计、调试、规划类任务切到 reasoning 更强的模型；固定工作流可以在 prompt files 或 custom agents 中 pin model。

> **案例：**需求澄清或架构迁移先用 reasoning model；批量生成模板代码时用更快的模型。

> **注意：**BYOK 只覆盖 chat，不覆盖 inline suggestions；即便使用本地或第三方模型，当前仍依赖 Copilot 服务，不等于完全离线。

> **原文：**[<u>Concepts - Language models</u>](https://code.visualstudio.com/docs/copilot/concepts/language-models)，[<u>Customization - AI language models</u>](https://code.visualstudio.com/docs/copilot/customization/language-models)

### 2. Context

> **作用：**上下文决定模型“看见什么”。Copilot 并不是默认理解你的整个仓库，而是通过自动检索和显式引用，把最相关的信息送进模型。

**关键机制：**\#file、#folder、#symbol、#codebase、#fetch、图片、终端输出、测试失败、Source Control 变更、browser element，以及会话压缩 /compact。

> **怎么用：**任务越模糊，越要显式补上下文；尽量只给相关上下文，不要把整个 session 污染得太杂；长对话及时 compact，避免早期无关信息干扰后续结果。

> **案例：**Explain how authentication works in \#codebase；Fix the failing tests \#testFailure。

> **注意：**上下文压缩会丢失细节；大仓库更依赖 indexing 和精确引用，而不是“多说点”。

> **原文：**[<u>Concepts - Context</u>](https://code.visualstudio.com/docs/copilot/concepts/context)，[<u>Chat - Manage context for AI</u>](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)

### 3. Tools

**作用：**模型只会生成文本，Tools 才让 Agent 真正能“干活”，比如读写文件、运行终端命令、调用 MCP server 或扩展提供的能力。

**官方定义的 3 类工具：**

|                |                |                                      |
| :-------------: | :------------: | :----------------------------------: |
| **类型** | **来源** |         **适合做什么**         |
| Built-in tools |  VS Code 内建  | 读写文件、终端、代码搜索、编辑器导航 |
|    MCP tools    |  MCP servers  |    数据库、API、浏览器、企业系统    |
| Extension tools |  VS Code 扩展  |           扩展深度集成能力           |

**配置位置：**

- Chat 输入框里的 **Configure Tools**：按请求临时启用/禁用工具。
- Prompt Files 的 frontmatter：tools。
- Custom Agents 的 frontmatter：tools。
- Prompt / Agent 正文中也可用 \#tool:\<tool-name\> 提示使用特定工具。

**为什么要主动控制工具：**

- 减少 context 消耗。工具输出本身也会进入上下文。
- 减少模型误调用无关工具的机会。
- 缩小决策空间，通常会更快。

**审批和信任：**

- 有副作用的工具会弹 approval prompt。
- URL 访问有双阶段批准流程。
- Permissions picker 决定 agent 的 autonomy level。

**最小示例：**

---

tools: \[read_file, grep_search\]

---

请先梳理认证链路，只允许读和搜索，不要修改代码。

**怎么扩展：**

1. 先用 Chat 里的 **Configure Tools** 做单次试验。
2. 确定流程稳定后，把同一组 tools 固化到 .prompt.md。
3. 如果这是长期角色边界，再把 tools 固化到 .agent.md。
4. 内建工具不够时，再补 MCP server 或 extension tools。

**案例：**让 planning agent 只有 read/search；让 implementation agent 再开放 edit/terminal；接外部系统时优先通过 MCP，而不是在 prompt 里堆大量外部数据。

**原文：**[<u>Concepts - Tools</u>](https://code.visualstudio.com/docs/copilot/concepts/tools)

### 4. Agents

**作用：**Agent 是 Copilot 从“回答你”走向“替你完成一件事”的核心。它会读取代码、拆步骤、执行、验证，并在失败时自修正。

**关键配置：**chat.agent.enabled、chat.autopilot.enabled、chat.planAgent.defaultModel、github.copilot.chat.implementAgent.model。

**怎么用：**复杂任务先用 Plan，再交给 Agent 执行；研究型问题可以交给 Subagent；长任务 handoff 到 CLI 或 Cloud。

**案例：**Create a plan to add a dark/light theme toggle to the app...

**注意：**Agent 功能可能受组织策略限制；Autopilot 和部分能力是 Preview。

**原文：**[<u>Concepts - Agents</u>](https://code.visualstudio.com/docs/copilot/concepts/agents)，[<u>Using agents in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/overview)

### 5. Customization

**作用：**Customization 决定 Copilot 是否真的“懂你的团队”。没有定制时，Copilot 更像泛化助手；有了定制后，它才更像团队内的高级工程师。

**怎么扩展 Copilot：**

1. 先用 /init 生成基础项目规则。
2. 再用 \*.instructions.md 细化语言 / 目录 / 模块规则。
3. 把高频单任务沉淀成 .prompt.md。
4. 把固定角色和工具边界做成 .agent.md。
5. 把带脚本、示例、资源的能力包做成 SKILL.md。
6. 需要接外部系统时再加 mcp.json。
7. 最后才引入 hooks 和 plugins。

**关键入口：Chat: Open Customizations**、Chat 视图里的齿轮按钮、/create-instruction、/create-prompt、/create-agent、/create-skill、/create-hook。

**关键配置：**chat.instructionsFilesLocations、chat.promptFilesLocations、chat.agentFilesLocations、chat.agentSkillsLocations、chat.hookFilesLocations、chat.useCustomizationsInParentRepositories。

**案例：**团队约定 Java 代码必须包含某种测试结构，就把约束写进 instruction files，而不是每次在 prompt 里重复；如果还需要固定成“只读 review persona”，再做 custom agent。

**注意：**custom instructions 不影响 inline suggestions，只影响 chat 和 agents。

**原文：**[<u>Concepts - Customization</u>](https://code.visualstudio.com/docs/copilot/concepts/customization)，[<u>Customize AI in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/overview)

### 6. Trust & Safety

**作用：**Trust & Safety 负责把控制权留给用户，而不是让 Agent 无限制行动。

**关键配置：**chat.permissions.default、chat.agent.sandbox.enabled、chat.agent.networkFilter、chat.agent.allowedNetworkDomains、chat.agent.deniedNetworkDomains。

**怎么用：**对高风险工具保持审批；对网络访问做 allow/deny 控制；对关键脚本、部署文件和敏感配置配合 review。

**案例：**允许 agent 读仓库、跑测试，但阻止它访问不在白名单中的网络域名。

**注意：**模型是非确定性的；Sandbox 当前主要覆盖终端命令，不等价于对所有行为完全隔离；Windows 上某些安全能力依赖 WSL2。

**原文：**[<u>Concepts - Trust and safety</u>](https://code.visualstudio.com/docs/copilot/concepts/trust-and-safety)

## 四、Agents：把 Copilot 从“会答”变成“会做”

### 1. Agents Overview

**作用：**官方把 Agents 定位成端到端任务执行器，适合跨文件实现、调试、迁移和验证。

**使用方式：**典型路径是 Ask/Plan 对齐需求，再切到 Agent 执行；长任务 handoff 到后台或云端；并行 session 处理独立任务。

**原文：**[<u>Using agents in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/overview)

### 2. Agents Tutorial

**作用：**帮助用户理解 agent 的实际工作循环，而不是只会下单句 Prompt。

**建议：**新用户至少完整走一遍 tutorial，再开始自定义自己的 workflow。

**原文：**[<u>Tutorial: Work with agents in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/agents-tutorial)

### 3. Agents Window (Preview)

**作用：**面向 agent-first 工作模式，适合同时管理多个 session 和多个项目。

**关键点：**支持 Changes 面板、集中看 customizations、连接远端机器；适合 prompt-first，不适合所有本地 agent 场景。

**注意：**这是 Preview；当前不支持本地 agent，只支持 Copilot CLI、Copilot Cloud、Claude agent 等特定后端。

**原文：**[<u>Use the Agents window</u>](https://code.visualstudio.com/docs/copilot/agents/agents-window)

### 4. Planning

**作用：**把“复杂任务直接让 AI 改代码”变成“先审计划，再执行”。

**入口位置：**

- Chat 面板中直接切到 **Plan** agent。
- 直接在输入框使用 /plan。

**Plan 阶段通常会产出：**

- 高层计划摘要
- 实施步骤
- 验证步骤
- 需要你确认的澄清问题

**关键配置：**

- chat.planAgent.defaultModel：指定 Plan agent 默认模型。
- github.copilot.chat.implementAgent.model：从规划切到实现时使用的模型。
- github.copilot.chat.planAgent.additionalTools：给 Plan 阶段增加额外工具（实验性）。

**计划保存在哪里：**

- Plan agent 会自动把计划保存到 /memories/session/plan.md。
- 查看入口：**Chat: Show Memory Files**。
- 这是 session memory，会话结束后清空。

**最小示例：**

/plan 为支付模块增加限流与重试，输出实施步骤、风险点、回滚方案和验证步骤。

**怎么扩展：**

1. 先让 Plan agent 只拿 read/search 类工具。
2. 确认过的计划，再从 /memories/session/plan.md 提炼到 repo memory 或项目文档。
3. 只有规划真的需要外部知识时，才给 github.copilot.chat.planAgent.additionalTools 增加工具。

**案例：**框架迁移、多模块重构、系统性性能优化。

**原文：**[<u>Planning with agents</u>](https://code.visualstudio.com/docs/copilot/agents/planning)

### 5. Memory

**作用：**让 Agent 不必每次从零开始理解你、理解仓库、理解当前任务。

**官方文档里有两种 memory：**

|                |                      |                    |                                                |
| :------------: | :-------------------: | :----------------: | :---------------------------------------------: |
| **类型** |    **范围**    | **存储位置** |              **适合做什么**              |
|  Memory tool  | User / Repo / Session |      本地机器      |        个人偏好、仓库约定、当前任务计划        |
| Copilot Memory |    Repository only    |    GitHub 托管    | 跨 cloud agent / code review / CLI 共享仓库知识 |

**Memory tool 配置：**github.copilot.chat.tools.memory.enabled。这是 Preview 功能，但文档说明默认启用。

**Memory scopes：**

- /memories/：User memory，跨工作区保留个人偏好。
- /memories/repo/：Repository memory，记录当前仓库的结构、约定、命令。
- /memories/session/：Session memory，记录当前对话里的临时计划和状态。

**管理入口：**

- **Chat: Show Memory Files**
- **Chat: Clear All Memory Files**

**Copilot Memory 配置：**github.copilot.chat.copilotMemory.enabled，并且需要先在 GitHub 侧启用 Copilot Memory。

**注意：**

- User memory 的前 200 行会自动加载到每次会话里。
- Plan agent 的 plan.md 属于 session memory，不会跨会话持久化。
- Copilot Memory 是仓库级共享记忆，28 天自动过期。

**最小示例：**

/memories/tooling.md

\- 默认先读 README、构建文件和测试入口

\- 修改后先跑最小范围验证

/memories/repo/conventions.md

\- DTO 放在 api 层，映射逻辑放在 mapper

\- 集成测试优先走统一测试命令

**怎么扩展：**

1. 个人习惯和偏好放 User memory。
2. 仓库事实和团队约定放 Repo memory。
3. 一次性计划和中间状态留在 Session memory。
4. 需要跨 GitHub surface 共享的仓库知识，再启用 Copilot Memory。

**原文：**[<u>Memory in VS Code agents</u>](https://code.visualstudio.com/docs/copilot/agents/memory)

### 6. Agent Tools

**作用：**决定 agent 能读什么、改什么、调用什么。

**使用方式：**对读文件、跑命令、浏览器、MCP、扩展工具进行按需开放；用审批保护高风险动作。

**原文：**[<u>Use tools with agents</u>](https://code.visualstudio.com/docs/copilot/agents/agent-tools)

### 7. Subagents

**作用：**把研究过程从主对话中隔离出去，避免污染主 session 上下文，并支持并行探索。

**什么时候该用：**

- 先研究再实现
- 并行分析多个方案
- 多角度代码评审
- 多模型交叉验证

**关键控制项：**

- 主 agent 要能使用 runSubagent 或 agent 工具。
- chat.subagents.allowInvocationsFromSubagents：是否允许 subagent 再调用 subagent。
- user-invocable：控制 custom agent 是否出现在下拉中。
- disable-model-invocation：控制 custom agent 是否允许被别的 agent 作为 subagent 调用。
- agents：在 .agent.md 中限定允许使用的 subagents。
- model：可在 subagent 或调用时指定模型。

**模型优先级：**调用时显式指定 \> subagent frontmatter 中的 model \> 主会话当前模型。

**最小示例：**

让 Research agent 先研究当前认证实现，输出候选方案、风险和推荐路径；不要改代码，结果返回主对话即可。

**怎么扩展：**

1. 先从一个只做 research 的 subagent 开始。
2. 稳定后，把它写成 .github/agents/research.agent.md，并设置 user-invocable: false。
3. 只有确实需要树形编排时，才打开 chat.subagents.allowInvocationsFromSubagents。

**案例：**“让 Research agent 先研究 auth 方案，再把结果交回主 agent”；“让 Plan agent 作为 subagent 先出实施计划，再保存到文件里”。

**原文：**[<u>Subagents in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/subagents)

### 8. Local Agents

**作用：**最适合交互式开发，因为能直接访问本地 VS Code 工作区、扩展、MCP、浏览器等上下文。

**使用方式：**需要边看边改、边验证边调整时，优先本地 agent。

**原文：**[<u>Local agents in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/local-agents)

### 9. Copilot CLI Sessions

**作用：**适合后台运行、worktree 隔离和长时间任务执行。

**关键配置：**github.copilot.chat.cli.remote.enabled、github.copilot.chat.cli.customAgents.enabled。

**使用方式：**本地探索完需求后，把清晰任务 handoff 到 CLI；必要时用 /remote on 把会话镜像到 GitHub / Mobile。

**注意：**CLI 没有全部 VS Code 内建工具，也没有 extension tools；它不能完全替代本地 agent。

**原文：**[<u>Copilot CLI sessions in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/copilot-cli)

### 10. Cloud Agents

**作用：**适合远程执行和基于 Pull Request 的团队协作。

**使用方式：**把实现交给云端 agent，在 GitHub 上产出分支和 PR，由团队审核。

**注意：**Cloud agent 无法直接读取你本地 editor/runtime 上下文。

**原文：**[<u>Cloud agents in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/cloud-agents)

### 11. Third-party Agents

**作用：**在 VS Code 中引入 Claude、OpenAI 等第三方 agent/provider 的差异化能力。

**关键配置：**github.copilot.chat.claudeAgent.enabled 等 provider 级开关。

**注意：**第三方 cloud agents 仍有 Preview 属性；部分“危险权限跳过”类能力只适合隔离环境。

**原文：**[<u>Third-party agents in VS Code</u>](https://code.visualstudio.com/docs/copilot/agents/third-party-agents)

## 五、Chat：最常用、也最容易被低估的中枢

### 1. Chat Overview

**作用：**Chat 是日常与 Copilot 交互的核心面板，负责对话、切 agent、切 model、补 context、管理 session。

**原文：**[<u>Chat overview</u>](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)

### 2. Chat Sessions

**作用：**把不同任务隔离成不同上下文，避免一个 session 混杂所有需求。

**使用方式：**复杂任务开新 session；思路分叉时 fork；长任务完成后归档；必要时导出 JSON 或保存为 prompt。

**原文：**[<u>Manage chat sessions</u>](https://code.visualstudio.com/docs/copilot/chat/chat-sessions)

### 3. Add / Manage Context

**作用：**决定 Chat 回答是否贴合你的仓库和当前问题。

**高价值上下文：**\#codebase、#changes、#problems、#testFailure、#fetch、图片、browser element。

**原文：**[<u>Manage context for AI</u>](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)

### 4. Inline Chat

**作用：**在当前编辑流中做小范围编辑，是“精准改代码”的最佳入口。

**关键配置：**inlineChat.defaultModel、inlineChat.askInChat、inlineChat.affordance。

**案例：**“给当前函数加 null 校验，但不要改公共接口”；“把这个逻辑改成流式写法”。

**原文：**[<u>Inline chat</u>](https://code.visualstudio.com/docs/copilot/chat/inline-chat)

### 5. Review Code Edits

**作用：**控制 AI 提交的代码变更是否真正落盘。

**关键配置：**chat.editing.autoAccept、chat.tools.edits.autoApprove。

**使用方式：**通过 Keep / Undo、敏感文件审批、差异审阅来控制风险。

**原文：**[<u>Review AI-generated code edits</u>](https://code.visualstudio.com/docs/copilot/chat/review-code-edits)

### 6. Checkpoints

**作用：**为 agent 编辑提供轻量级回滚点。

**关键配置：**chat.checkpoints.enabled、chat.checkpoints.showFileChanges。

**注意：**官方明确说 checkpoints 不能替代 Git，只是便于快速回退和重新编辑请求。

**原文：**[<u>Revert changes with checkpoints and editing requests</u>](https://code.visualstudio.com/docs/copilot/chat/chat-checkpoints)

### 7. Artifacts Panel (Preview)

**作用：**把截图、计划、文档等产物集中展示，方便跟踪 agent 工作结果。

**关键配置：**chat.artifacts.enabled。

**原文：**[<u>Artifacts panel</u>](https://code.visualstudio.com/docs/copilot/chat/chat-artifacts)

### 8. Debug Chat Interactions

**作用：**排查为什么 prompt file 没生效、为什么某个上下文没进模型、为什么某个工具没被调用。

**关键配置：**github.copilot.chat.agentDebugLog.fileLogging.enabled。

**原文：**[<u>Debug chat interactions</u>](https://code.visualstudio.com/docs/copilot/chat/chat-debug-view)

### 9. Prompt Examples

**作用：**帮助用户把“模糊需求”改写成“可执行需求”。

**建议：**Prompt 尽量包含输入、输出、约束、验证标准。

**原文：**[<u>Prompt examples</u>](https://code.visualstudio.com/docs/copilot/chat/prompt-examples)

## 六、Customization：让 Copilot 真正适应你的团队

### 1. Overview

**建议顺序：**Instructions → Prompt Files → Custom Agents → Skills → MCP → Hooks → Plugins。不要一上来就把最复杂的机制全堆上去。

**统一管理入口：Chat: Open Customizations** 或 Chat 面板里的齿轮按钮。这里能集中管理 Instructions、Prompts、Agents、Skills、Hooks、MCP、Plugins。

**Parent repository discovery：**如果是 monorepo 或只打开子目录，开启 chat.useCustomizationsInParentRepositories 后，VS Code 会向上找到带 .git 的 repo root，并发现根目录上的 instructions、prompts、agents、skills、hooks。

**原文：**[<u>Customize AI in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/overview)

### 2. Custom Instructions

**作用：**项目长期规则、编码约定、架构背景、环境约束。

**主要文件位置：**

- .github/copilot-instructions.md：workspace 级 always-on instructions。
- .github/instructions/\*\*/\*.instructions.md：按语言 / 文件类型 / 模块细分。
- AGENTS.md：workspace root 的 always-on instructions。
- CLAUDE.md、.claude/CLAUDE.md、~/.claude/CLAUDE.md：兼容 Claude 工具链。

**关键 settings：**

- chat.instructionsFilesLocations：自定义 instructions 搜索目录。
- chat.useAgentsMdFile：启用 AGENTS.md。
- chat.useNestedAgentsMdFiles：启用多个嵌套 AGENTS.md（实验性）。
- chat.useClaudeMdFile：启用 CLAUDE.md。
- github.copilot.chat.organizationInstructions.enabled：启用组织级 instructions。
- chat.includeApplyingInstructions / chat.includeReferencedInstructions：控制 pattern-based 与引用型 instructions 是否加入上下文。

**文件格式核心：**.instructions.md 支持 YAML frontmatter，最关键的是 applyTo，用于按 glob 自动匹配文件。

**创建入口：**/init、/create-instruction、/instructions、**Chat: New Instructions File**。

**优先级：**个人 instructions \> 仓库 instructions \> 组织 instructions。

**注意：**custom instructions **不影响** inline suggestions。

**最小示例：**

---

applyTo: "\*\*/\*.java"

---

\- 优先沿用现有 controller / service / mapper 分层

\- 新增接口必须补单元测试

\- 除非用户明确要求，不要改 public API 名称

**怎么扩展：**

1. 先在 .github/copilot-instructions.md 写全局规则。
2. 当不同语言或目录规则不一样时，再拆成多个 .instructions.md。
3. 多 agent 共用规则时再补 AGENTS.md；要兼容 Claude 生态时再补 CLAUDE.md。

**原文：**[<u>Use custom instructions in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

### 3. Prompt Files

**作用：**把高频、单次任务固化成可复用 slash command。

**文件位置：**

- Workspace：.github/prompts
- User：当前 VS Code profile 的用户数据目录

**关键 setting：**chat.promptFilesLocations。如需新会话推荐 prompts，可用 chat.promptFilesRecommendations。

**常用 frontmatter 字段：**name、description、argument-hint、agent、model、tools。

**创建和使用入口：**/create-prompt、/prompts、**Chat: New Prompt File**，以及直接在聊天框输入 /\<prompt-name\>。

**关键规则：**如果 prompt file 和 custom agent 都定义了 tools，则 **prompt file 优先**。

**适合场景：**生成组件、生成 PR 描述、执行安全检查模板、生成测试计划、固定 API 脚手架。

**最小示例：**

---

name: gen-test-plan

description: 根据需求输出测试清单

agent: ask

tools: \[read_file, grep_search\]

---

请根据我给出的需求和代码上下文，输出测试场景、边界条件和验收点。

**怎么扩展：**

1. 先把一条高频 prompt 固化成 slash command。
2. 如果需要固定角色或 handoff，再把 agent 从内建 agent 升级成 custom agent。
3. 如果 prompt 还需要脚本、示例或资源，再升级成 skill。

**原文：**[<u>Use prompt files in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/prompt-files)

### 4. Custom Agents

**作用：**把特定角色、工具集合、模型约束固定下来，例如 TDD agent、security review agent、docs writer agent。

**文件位置：**

- Workspace：.github/agents
- Claude 兼容：.claude/agents
- User：~/.copilot/agents

**关键 settings：**

- chat.agentFilesLocations：扩展 custom agent 搜索目录。
- github.copilot.chat.organizationCustomAgents.enabled：启用组织级 custom agents。
- chat.useCustomAgentHooks：允许 custom agents 使用 scoped hooks。

**关键 frontmatter 字段：**tools、agents、model、user-invocable、disable-model-invocation、handoffs、hooks。

**Handoffs 的意义：**允许一个 agent 结束后，直接把用户切换到另一个 agent，并带上预填 prompt，例如 Planning → Implementation → Review。

**创建入口：**/create-agent、/agents、**Chat: New Custom Agent**。

**最小示例：**

---

description: 只做只读代码评审

tools: \[read_file, grep_search\]

user-invocable: true

---

请聚焦 bug、回归风险和缺失测试，默认不要修改代码。

**怎么扩展：**

1. 先固定 persona 和 tools。
2. 稳定后再补 agents 和 handoffs，把 Planning → Implementation → Review 串起来。
3. 只有需要生命周期自动化时，再给这个 agent 加 hooks。

**原文：**[<u>Custom agents in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

### 5. Agent Skills

**作用：**Skills 不是规则，而是**能力包**。它可以带脚本、示例、资源，并且可跨 VS Code、Copilot CLI、Copilot Cloud agent 复用。

**文件位置：**

- Project：.github/skills/、.claude/skills/、.agents/skills/
- User：~/.copilot/skills/、~/.claude/skills/、~/.agents/skills/

**关键 settings：**

- chat.agentSkillsLocations：扩展 skills 搜索目录。
- github.copilot.chat.skillTool.enabled：启用 context: fork 的 forked-context skills（实验性）。

**SKILL.md 关键字段：**name、description、argument-hint、user-invocable、disable-model-invocation、context。

**重要规则：**

- name 只能是小写字母、数字、连字符。
- name 必须与目录名一致，否则 skill 会静默不加载。
- 如果 skill 引用了脚本或示例文件，必须在 SKILL.md 中用 Markdown 链接引用，agent 才会按需加载。

**context: fork 的意义：**让 skill 在独立 subagent context 中运行，避免把大量中间过程污染主对话。

**创建入口：**/create-skill、/skills。

**最小示例：**

.github/skills/api-debug/SKILL.md

---

name: api-debug

description: 排查 API 失败并输出根因与验证步骤

---

读取日志样例、错误码说明和排查步骤，输出根因分析和验证建议。

**怎么扩展：**

1. 先把稳定的操作说明写进 SKILL.md。
2. 需要脚本、样例或模板时，放在同目录，并在 SKILL.md 里用 Markdown 链接引用。
3. 中间过程很长或很脏时，再考虑 context: fork。

**原文：**[<u>Use Agent Skills in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

### 6. Language Models

**作用：**在定制层面对不同任务绑定不同模型，而不是所有任务都共享一个默认模型。

**管理入口：**Chat 输入框的 model picker，或 **Chat: Manage Language Models**。

**关键功能：**显示/隐藏模型、pin favorite models、Auto model selection、thinking effort、BYOK。

**关键文件：**chatLanguageModels.json，用于自定义 provider、custom endpoint、model capabilities。

**原文：**[<u>AI language models in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/language-models)

### 7. MCP Servers

**作用：**把数据库、API、浏览器、内部平台、CLI 等外部能力接给 Copilot。

**配置位置：**

- Workspace：.vscode/mcp.json
- User profile：通过 **MCP: Open User Configuration** 打开的 mcp.json
- Remote user：**MCP: Open Remote User Configuration**

**关键入口：MCP: Add Server**、Extensions 搜索 @mcp、Chat 的 Add Context \> MCP Resources。

**关键 setting：**chat.mcp.autoStart，用于配置变更后自动重启 MCP server（实验性）。

**MCP 不只提供 tools，还可以提供：**

- Resources：作为只读上下文附加到 prompt
- Prompts：使用 /\<MCP server\>.\<prompt\>
- MCP Apps：在 chat 中渲染交互 UI

**重要安全点：**

- 本地 MCP server 可以执行任意代码，只能从可信来源安装。
- Windows 当前**不支持** MCP sandboxing。
- 如果直接从 mcp.json 启动，文档明确说不会弹 trust prompt。

**原文：**[<u>Add and manage MCP servers in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

### 8. Hooks (Preview)

**作用：**在生命周期节点自动运行命令，用于自动化和策略 enforcement。

**典型事件：**SessionStart、UserPromptSubmit、PreToolUse、PostToolUse、PreCompact、SubagentStart、SubagentStop、Stop。

**配置位置：**

- Workspace：.github/hooks/\*.json
- User：~/.copilot/hooks
- Claude 兼容：.claude/settings.json 等
- Agent scoped：写进 .agent.md 的 hooks 字段

**关键 settings：**chat.hookFilesLocations、chat.useCustomAgentHooks。

**适用场景：**自动格式化、PreToolUse 安全拦截、PostToolUse 校验、SessionStart 注入环境信息。

**注意：**hooks 能执行本地命令，是很强也很危险的能力。一定要对 hooks 文件和其调用脚本做严格 review。

**原文：**[<u>Agent hooks in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/hooks)

### 9. Plugins (Preview)

**作用：**把 agents、skills、hooks、MCP servers 等能力打包分发。

**关键配置：**

- chat.plugins.enabled：是否启用 agent plugins。
- chat.plugins.marketplaces：配置 plugin marketplace。
- chat.pluginLocations：本地 plugin 位置及启用状态。

**适合场景：**团队要统一分发一整套 Copilot 自定义能力时。

**注意：**Plugins 是 Preview；命名和目录错误时，也可能表现为静默不生效。

**原文：**[<u>Agent plugins in VS Code</u>](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)

## 七、最值得背下来的三个比较

### 1. Ask vs Inline Chat vs Agent vs Plan

|                |                      |                          |
| :------------: | :------------------: | :----------------------: |
| **模式** |    **定位**    |    **最佳场景**    |
|      Ask      |   问答、理解、探索   |   先搞清楚系统怎么工作   |
|  Inline Chat  |   当前文件精准编辑   |        小范围改动        |
|     Agent     |    多文件自治执行    |         真正做事         |
|      Plan      | 先规划、不急着写代码 | 复杂方案、迁移、架构改造 |

### 2. Local vs CLI vs Cloud vs Third-party

|                |                        |                      |                                |
| :------------: | :---------------------: | :------------------: | :----------------------------: |
| **类型** |     **优势**     |  **适合场景**  |         **限制**         |
|     Local     |  上下文最全，交互最强  |    边改边看边验证    |           需要你在场           |
|      CLI      | 适合后台、worktree 隔离 |  长任务、非阻塞执行  | 没有全部 VS Code 工具/扩展工具 |
|     Cloud     |    适合团队协作和 PR    | 远程实现、代码审查流 |         缺少本地上下文         |
|  Third-party  | 可用不同 provider 能力 |  需要特定模型风格时  |        部分仍是 Preview        |

### 3. Instructions vs Prompt Files vs Custom Agents vs Skills

|                |                            |
| :------------: | :------------------------: |
| **机制** | **最适合解决的问题** |
|  Instructions  |     长期规则和项目约束     |
|  Prompt Files  |    可反复执行的任务模板    |
| Custom Agents |  固定角色、模型和工具组合  |
|     Skills     |        可移植能力包        |

## 八、Best Practices：真正提高成功率的做法

1. **先优化项目，再抱怨 AI。** 先做 /init，再补最关键的 instructions。
2. **为任务选对交互面。** 小任务不要上 Agent，复杂任务不要只靠 Inline Chat。
3. **Prompt 要具体。** 写清输入、输出、约束、验证标准。
4. **上下文越精准越好。** 用 \#file / \#codebase / \#fetch，不要靠冗长自然语言硬堆背景。
5. **复杂任务先 Plan。** 先对齐方案，再执行。
6. **始终 review 和 verify。** 跑测试、看 diff、查安全边界，不能把 AI 输出直接当真。
7. **大仓库拆任务、拆 session、并行跑。**
8. **尽早纠偏。** 发现 AI 跑偏，立刻 follow-up 或 fork，不要把错误路线越走越深。

**官方最佳实践原文：**[<u>Best practices for using AI in VS Code</u>](https://code.visualstudio.com/docs/copilot/best-practices)

## 九、最有价值的命令 / 动作

- /init：生成项目级 always-on instructions。
- /plan：让 Plan agent 先出执行方案。
- /compact：压缩长会话上下文。
- /fork：从当前 session 分叉。
- /savePrompt：把有效对话沉淀为 prompt file。
- /create-instruction、/create-prompt、/create-agent、/create-skill、/create-hook：把一次性经验变成长期资产。
- /instructions、/prompts、/agents、/skills、/hooks：快速打开相应管理入口。
- /remote on / /remote off：镜像 Copilot CLI session。
- /delegate：把后台 session 交给 Cloud agent。

## 十、推荐采用路线

1. **第 1 阶段：先学 Ask + Inline Chat。** 先会问、会给上下文、会做局部修改。
2. **第 2 阶段：引入 Agent + Plan。** 让 Copilot 开始处理跨文件任务。
3. **第 3 阶段：执行一次 /init。** 用最小但高价值的 instructions 提升命中率。
4. **第 4 阶段：沉淀 Prompt Files / Custom Agents / Skills。** 把重复动作产品化。
5. **第 5 阶段：再扩到 CLI / Cloud / MCP / Hooks。** 当基础流程跑顺后，再扩大自动化边界。

## 十一、容易忽略但很重要

- Custom instructions 不影响 inline suggestions。
- Parent repository discovery 默认关闭；在 monorepo 里不开它，很多根目录定制会“看不见”。
- Prompt file 里指定的 tools 优先级高于 custom agent 里的 tools。
- Cloud agent 和 CLI agent 都不能完全替代 Local agent，因为它们拿不到同样完整的本地上下文和工具面。
- Skills / Plugins / Hooks 命名和目录不合法时，可能表现为“静默不生效”，这类问题要优先去看 debug view。
- MCP server 如果直接从 mcp.json 启动，文档明确说不会弹 trust prompt。
- Hooks、Plugins、MCP 都可能执行本地代码；如果 agent 还能改这些脚本，就必须配合敏感文件审批和严格 review。

## 十二、原始链接总表

- [<u>Overview</u>](https://code.visualstudio.com/docs/copilot/overview)
- [<u>Concepts Overview</u>](https://code.visualstudio.com/docs/copilot/concepts/overview)
- [<u>Concepts - Language models</u>](https://code.visualstudio.com/docs/copilot/concepts/language-models)
- [<u>Concepts - Context</u>](https://code.visualstudio.com/docs/copilot/concepts/context)
- [<u>Concepts - Tools</u>](https://code.visualstudio.com/docs/copilot/concepts/tools)
- [<u>Concepts - Agents</u>](https://code.visualstudio.com/docs/copilot/concepts/agents)
- [<u>Concepts - Customization</u>](https://code.visualstudio.com/docs/copilot/concepts/customization)
- [<u>Concepts - Trust and safety</u>](https://code.visualstudio.com/docs/copilot/concepts/trust-and-safety)
- [<u>Agents - Overview</u>](https://code.visualstudio.com/docs/copilot/agents/overview)
- [<u>Agents - Tutorial</u>](https://code.visualstudio.com/docs/copilot/agents/agents-tutorial)
- [<u>Agents - Agents window</u>](https://code.visualstudio.com/docs/copilot/agents/agents-window)
- [<u>Agents - Planning</u>](https://code.visualstudio.com/docs/copilot/agents/planning)
- [<u>Agents - Memory</u>](https://code.visualstudio.com/docs/copilot/agents/memory)
- [<u>Agents - Tools</u>](https://code.visualstudio.com/docs/copilot/agents/agent-tools)
- [<u>Agents - Subagents</u>](https://code.visualstudio.com/docs/copilot/agents/subagents)
- [<u>Agents - Local agents</u>](https://code.visualstudio.com/docs/copilot/agents/local-agents)
- [<u>Agents - Copilot CLI</u>](https://code.visualstudio.com/docs/copilot/agents/copilot-cli)
- [<u>Agents - Cloud agents</u>](https://code.visualstudio.com/docs/copilot/agents/cloud-agents)
- [<u>Agents - Third-party agents</u>](https://code.visualstudio.com/docs/copilot/agents/third-party-agents)
- [<u>Chat overview</u>](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- [<u>Chat sessions</u>](https://code.visualstudio.com/docs/copilot/chat/chat-sessions)
- [<u>Chat context</u>](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)
- [<u>Inline chat</u>](https://code.visualstudio.com/docs/copilot/chat/inline-chat)
- [<u>Review code edits</u>](https://code.visualstudio.com/docs/copilot/chat/review-code-edits)
- [<u>Checkpoints</u>](https://code.visualstudio.com/docs/copilot/chat/chat-checkpoints)
- [<u>Artifacts</u>](https://code.visualstudio.com/docs/copilot/chat/chat-artifacts)
- [<u>Debug chat interactions</u>](https://code.visualstudio.com/docs/copilot/chat/chat-debug-view)
- [<u>Prompt examples</u>](https://code.visualstudio.com/docs/copilot/chat/prompt-examples)
- [<u>Customization overview</u>](https://code.visualstudio.com/docs/copilot/customization/overview)
- [<u>Custom instructions</u>](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [<u>Prompt files</u>](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [<u>Custom agents</u>](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [<u>Agent skills</u>](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [<u>Customization - Language models</u>](https://code.visualstudio.com/docs/copilot/customization/language-models)
- [<u>MCP servers</u>](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [<u>Hooks</u>](https://code.visualstudio.com/docs/copilot/customization/hooks)
- [<u>Plugins</u>](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)
- [<u>Best practices</u>](https://code.visualstudio.com/docs/copilot/best-practices)
