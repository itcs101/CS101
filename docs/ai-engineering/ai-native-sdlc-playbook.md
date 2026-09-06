# AI 原生 SDLC 手册（The AI-Native SDLC Playbook）

如何利用 AI 逐步改造软件开发生命周期。

> 原文：[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)（Claude 官方博客）
> 作者：Louis Claxton ｜ 类别：Enterprise AI / Claude Code / Product / Claude Enterprise / Claude Tag ｜ 日期：2026-08-21 ｜ 阅读时间：46 分钟

## 目录

- [代码不再是瓶颈](#代码不再是瓶颈)
- [什么是 AI 原生 SDLC？](#什么是-ai-原生-sdlc)
- [剧本（Plays）](#剧本plays)
- [01 计划（Plan）](#01-计划plan)
- [02 设计（Design）](#02-设计design)
- [03 构建（Build）](#03-构建build)
- [04 测试（Test）](#04-测试test)
- [05 部署（Deploy）](#05-部署deploy)
- [06 维护（Maintain）](#06-维护maintain)
- [结语](#结语)

## 代码不再是瓶颈

各组织已经开始使用 AI 并以一年前难以想象的速度编写代码，然而围绕代码的流程却没有以同样的速度发生变化。

许多工程团队仍然沿用相同的**审批门禁（approval gates）、审查、交接和政策**，阻碍了使用 Claude Code 等智能编码解决方案所带来的生产力提升。

软件开发生命周期 (SDLC) 是将软件从构思到最终生产的整个过程。大多数组织都会遵循类似的六个阶段，涵盖**规划、设计、构建、测试、部署和维护软件**。传统上，每个阶段都是一个独立的步骤，由不同的角色负责。产品经理编写需求，技术架构师将需求转化为设计，工程师构建设计，受监管企业的质量保证团队进行验证，发布团队负责发布，运维团队负责监控软件的运行状态。工作在各个阶段之间通过文档、工单和签字确认进行流转。

传统的软件开发生命周期（SDLC）流程繁多，旨在确保每个步骤的责任落实和控制。然而，传统的 SDLC 设计初衷是为了在编写和实现代码这一耗时耗力的时代最大限度地提高效率，而如今情况已大不相同。产品需求文档（PRD）、估算流程（estimation rituals）和产品安全审查等都是为了在可能持续数周、数月甚至数个季度的开发工作中强制执行一致性。

传统的软件开发生命周期（SDLC）中的控制措施假定每个步骤都由人工执行。而那些创造最大价值的组织已经围绕智能 AI 的强大功能重构了流程，同时确保人工参与其中。在本指南中，我们将介绍应用 AI 团队在 SDLC 各个阶段集成 Claude 的几项最佳实践，这些实践旨在加速开发并提高流程效率，其灵感来源于我们与客户的合作。

当代码不再是瓶颈，并且构建阶段的运行速度超过了传统软件开发生命周期所允许的速度时，以下三件事就会成为现实：

- 瓶颈转移到了构建阶段左右两侧的步骤。这些步骤主要包括**计划、评审/测试和部署**，而这些步骤的执行速度仍然取决于人的速度。
- 控制方式不再符合实际情况，变得难以操作。当代码是由人编写时，逐行手动检查是有意义的，但一旦大部分代码修改（git diff）由人工智能代理（agent）编写，这种方法就无法跟上了。
- 由于例外情况仍需通过每周或每月召开的会议和委员会进行审批，因此治理成本会增加。

![构建不再是约束——它周围的、以人为速度运行的步骤才是。以人为速度运行的阶段保持其时长，而构建过程则缩短至数小时。](asset/img/sdlc-bottleneck.png)

我们以安全瓶颈为例。安全团队的规模是根据人力产出来定的，因此当人工智能代理使代码产出成倍增长时，要么审查队列不断积压，要么代码未经充分审查就被发布。受监管的组织无法接受这两种结果，因此其安全和策略检查必须跟上人工智能代理的步伐。

为了更好地实现智能 AI 的生产力提升并确保其安全，传统的软件开发生命周期需要像实施阶段一样进行同等程度的变革。

## 什么是 AI 原生 SDLC？

AI 原生 SDLC 是一种重新构想的流程，它将传统的控制目标与新的执行机制相结合。该流程不再是线性流程，而是一个循环，并且在每个环节都嵌入了 AI。AI 原生 SDLC 促进了后续操作的自动交接和触发，有助于解决传统 SDLC 各阶段之间手动交接的繁琐问题。

你还会听到这种转变被称为「代理式 SDLC（agentic SDLC）」「AI SDLC」或简称为「代理式软件开发（agentic software development）」——标签不同，但它们描述的是同一件事。

![AI 原生 SDLC 循环：六个阶段各自提交一个工件，供下一阶段读取](asset/img/ai-native-sdlc-loop.png)

### 六个阶段的转变

下表突出了传统软件开发生命周期 (SDLC) 和由 Claude 支持的 AI 原生 SDLC 之间的差异。大多数组织的情况介于这两列之间。

| 阶段 | 传统软件开发生命周期                                                             | AI 原生软件开发生命周期                                                                                                            |
| ---- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 计划 | 委员会收集的需求，经研讨会和签字确认后提炼，并手工记录下来。                     | Claude 直接从源头提炼痛点，并将其捕捉到`intent.md` 中——既易于人理解又可供机器操作的格式。                                      |
| 设计 | 分析师编写的规范，由设计师解读。                                                 | 需求和设计被压缩到与人工智能代理的一次工作会议中，遵循以技能形式编码的标准，并在 Git 中进行版本控制。                              |
| 构建 | 测试和代码都是手工编写的，文档是在主要开发完成后才编写的。                       | 测试和代码由 AI 生成，机构知识以版本化的机器可读`CLAUDE.md` 文件和技能的形式维护。                                               |
| 测试 | 阶段边界的质量保证关卡。                                                         | 实施过程中贯穿持续评估。                                                                                                           |
| 部署 | 人工会审查每一行代码，代码治理也以审查周期的形式进行，但这种周期往往缺乏一致性。 | 多层人工智能代理审查，**人工审查保留给受监管的关键代码**。治理机制在 AI 运行过程中逐步实施，并**通过钩子作为审批门**。 |
| 维护 | 人类会监控生产过程，以发现缺陷。                                                 | 人工智能代理会监控实时部署。任何被突破的控制带都会被诊断出来，并作为新的`intent.md` 重新写入循环中。                             |

右侧一列贯穿始终的主线是**已提交的工件**。每个阶段结束时，都会向版本控制系统写入一个工件（包括 `intent.md`、`spec.md`、`plan.md`、差异及其测试、包含审查结果的 PR 以及事件记录），下一阶段则从中读取该工件。在早期阶段，`.md` 文件是主要的工件，因为产品负责人和人工智能代理都可以读取并操作同一个文件。从构建阶段开始，工件就变成了代码及其记录。提交链也构成了审计跟踪：记录了谁提出了什么请求、人工智能代理生成了什么以及谁批准了它。

人类始终对每一项需要判断的决策负责。在人工智能代理驱动的软件开发生命周期（SDLC）中，人类的注意力会随着需要审查的工件而转移。

> 每个阶段都会提交一个工件，供下一阶段读取。意图、规范、计划、差异和评审结果共同构成了审计跟踪。

## 剧本（Plays）

这些剧本（play）是手册的核心，分为六个非线性阶段（计划、设计、构建、测试、部署、维护），共同涵盖了整个生命周期。

每个剧本都包含以下内容：

- 哪些方面发生了变化；
- 入门；
- 具体实施步骤；
- 治理方面的考虑；以及
- 如何衡量它是否有效。

这些步骤是模块化的，组织可以根据自身独特的需求，选择在不同时间优先改造不同的阶段。每个步骤都在「先决条件」下列出了其依赖项，依赖关系图对此进行了更详细的说明。

一个阶段以提交工件结束，该提交会启动下一个阶段。一个被接受的 `intent.md` 工件会触发需求和设计流程，一个被批准的 `spec.md` 工件会触发计划模式，一个合并的 PR 会触发流水线，而生产环境中的某个控制带被突破则会写入下一个 `intent.md` 工件，如此循环往复。

首先，你需要手动提示每个步骤，最终状态是一个循环，其中每个被接受的工件都会触发下一个门。人类的注意力集中在门上，回顾人工智能代理标记的内容，而不是从头开始每个阶段。

![各剧本按阶段列出；箭头指示采用顺序。两者并不相同。先从任何一个「黏土剧本」（无依赖的剧本）开始——没有箭头指向它，说明它不需要任何先决条件。对于其他任何剧本，指向它的箭头指示的是它之前需要采用的剧本。](asset/img/plays-adoption-order.png)

## 01 计划（Plan）

创意不会等待别人将其记录下来。意图只需用创作者自己的语言记录一次，便会成为版本控制的文档，供下一阶段使用。

### 以 intent.md 捕获创意意图

`intent.md` 启动软件开发流程的事件可以通过不同的途径进入。例如，有人提出想法、提交工单，或者通过警报发现问题（参见阶段 6：维护）。

当一个人有了想法后，他会和 Claude 一起进行头脑风暴，并生成一个 Markdown 格式的原型规范。在传统的软件开发生命周期中，这个人随后必须说服产品团队的成员与他一起或代表他把这个想法写成文档。

Claude 生成的原型规范是人类可读的，版本可控，并且可以立即被下一阶段使用。该原型规范保存为 `intent.md`。

无论意图是源自事件触发器还是人工智能代理，步骤都相同：产品负责人会在提交之前审查并纠正人工智能代理编写的 `intent.md`。

> **传统方式**：一个想法在最终付诸行动之前，需要经过待办事项列表、用户故事、故事点和需求细化会议等一系列流程。每次交接都会发生所有权转移，因此最终到达工程团队的版本与最初提出者的意图往往相去甚远。
>
> **AI 原生方式**：发起人与 Claude 进行头脑风暴，并将结果记录为 `intent.md`，形成一份以发起人自身语言编写的原型规范。该规范包含了所需内容、原因以及约束条件。重复性流程通过技能进行编码。

**入门**：

- **先决条件**：没有任何。
- **基础设施**：对于非工程师用户，可以通过 claude.ai 或 [Cowork](https://claude.com/product/cowork) 访问 Claude；需要一个约定的 `intent.md` 模板；需要一个共享的、版本控制的创意存放处，由产品负责人监控。对于单个产品，最简单的存放处是产品代码库中的一个 `intent/` 文件夹，这样可以把工件链与派生自它的代码放在一起。只有当意图跨越多个代码库时，专用的意图仓库才值得投入额外的开销，而在单体仓库中，它只是一个目录。「阶段 3：构建」的侧边栏介绍了此存放处与已经持有记录的 Jira 或需求工具之间的关系。搭建此存放处是平台或工程团队的一次性任务：一名技术团队成员需要创建意图存放处，并决定谁可以向其中写入内容，因为许多贡献者将来自组织的各个部门。
- 仓库创建完成后，没有 Git 经验的贡献者无需直接使用 Git。Claude 会**通过与版本控制系统（例如 GitHub）的连接器**，代表他们从 claude.ai 或 Cowork 提交 Markdown 文件。

**如何执行**：

1. 提出问题的人用自己的语言向 Claude 描述问题。提出问题的人可以描述目前无法解决的问题、哪些人会受到该想法的影响、更好的解决方案是什么，或者哪些内容超出了讨论范围。无需使用正式的语言。
2. 集思广益，直到想法具体化。**Claude 提出了分析师会问的问题**：范围、用户、限制条件以及成功的标准。
3. 请 Claude 使用组织提供的模板撰写结果报告 `intent.md`，该模板可由技术团队成员编码为一项技能，并由负责人签字确认。报告内容应涵盖问题、预期结果、受影响的用户和系统、限制条件以及未决问题。
4. 原作者纠正 Claude 的任何误解。
5. 提交 `intent.md` 到共享的意图存放处。作者和时间戳会添加到记录中，产品负责人可以从这里继续完善想法。

**长什么样（intent.md）**：

```markdown
# Intent: claims status self-service

Author: J. Ortiz (claims operations). Status: draft.

## Problem

Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.

## Proposed outcome

Customers see claim status, next step and expected date in the portal.

## Affected users and systems

Claims handlers, portal team, claims-core API.

## Constraints

No new PII in the portal session. Existing authentication only.

## Open questions

Do third-party loss adjusters need access too?
```

**治理方面的考虑**：证据是已提交的 `intent.md`，其中列出了作者、时间戳和完整的修订历史，并记录在意图存放处的 Git 历史中。产品负责人负责批准；把意图送入第二阶段：设计的接受或拒绝决定，被记录为合并或关闭的评审。

**如何测量**：

- **领先指标**：从首次对话到提交 `intent.md` 的时间，可以从意图存放处的 Git 历史中读取，其中记录了作者和时间戳。预期目标是将原本需要数周的收集和完善周期缩短到数小时。
- **滞后指标**：存活率，即被产品负责人接受进入第二阶段（设计）而不是被关闭的 `intent.md` 所占比例。接受或拒绝的决定记录为工件的合并或评审的关闭。此外，还包括同一变更在首次提交 `spec.md` 之后对 `intent.md` 所做的更改次数。

## 02 设计（Design）

需求和设计在一次会议中完成。策略在编写规范时就已应用，而不是在几周后的评审中才发现。

### 需求与设计

经产品负责人批准后，Claude 根据已接受的 `intent.md` 制定需求和设计规范。这需要结合组织在品牌、安全、合规和用户体验方面的能力。

产品负责人审核该规范，但不参与编写。此流程的目标是创建一份工程团队可以据此进行规划的规范，并标明需要关注的领域。

前端开发就是最明显的例子。一旦 `intent.md` 被接受，产品负责人就在 [Claude Design](https://claude.com/product/design)（测试版）中根据 `intent.md` 制作设计原型，不断迭代修改，然后将其导出到 Claude Code 进行构建。

> **传统方式**：需求分析和设计是两个独立的阶段，分别由不同的团队负责。分析师将想法提炼成需求，设计师再将需求解析成设计方案。这种分离是为了明确责任，但效率低下且容易造成信息损失。
>
> **AI 原生方式**：这两个阶段都在一次引导式会议中完成。Claude 以 `intent.md` 为基础，结合组织的技能，生成需求和设计规范，并标记出需要关注的领域。

**入门**：

- **先决条件**：一份 `intent.md` 文件，并将品牌、安全、合规和用户体验策略编写为技能。
- **基础设施**：拥有 Claude 访问权限的产品负责人。无需任何工程技能。

**如何执行**：

1. 产品负责人打开一个**可加载组织技能**的会话，并附上 `intent.md`。
2. 产品负责人的提示指向 `intent.md`，列出约束条件，并要求标记出需要关注的问题。先手工运行，然后把它固化为组织级的斜杠命令（slash command）。之后，将意图存放处中 `intent.md` 的接受作为触发条件，用一个非交互式作业在合并时触发，加载组织技能运行该流程，并将 `spec.md` 以拉取请求的形式提交（阶段 5：部署中的 CI/CD 流程涵盖了底层架构）。从那时起，产品负责人的首次参与就是评审。
3. 同一位产品负责人对照原始想法审查规范：规范是否解决了既定问题？`intent.md` 中提出的未决问题是被解答了，还是被保留了下来？
4. 首先处理已标记的问题，因为这些问题是分析师通常会上报的。产品负责人会在工程团队查看规范之前，与相应的策略负责人解决每个问题。
5. 将 `spec.md` 与 `intent.md` 一同提交。这一对文件记录了请求的内容和最终决定的内容。
6. 产品负责人决定规范和意图是否进入构建阶段，对于组织认为风险较高的任何事项，都会咨询技术负责人。这项决定始终由团队中的人做出，而接受规范即启动第三阶段：构建中的计划模式剧本。

**长什么样（提示）**：

```text
Read the attached intent.md and produce a requirements and design spec for integrating it into our existing codebase. Apply the skills available to you so the plan conforms to our brand guidelines, security policies and UX standards. Document the spec fully as spec.md, ready to hand to the engineering team. Describe clearly any areas of concern, especially where you cannot satisfy contradicting policies.
```

**治理方面的考虑**：现行策略并非在数周后的评审中才被发现，而是在编写规范的同时就被阅读并应用。组织的技能作为规范的约束条件。规范、生成规范的提示以及生效的技能版本都会被记录在版本控制系统中。产品负责人签署规范，并将标记的问题反馈给指定的策略负责人。

**如何测量**：

- **领先指标**：同一变更从 `intent.md` 提交到 `spec.md` 提交之间的时间间隔（两个 git 时间戳），与旧的需求加设计周期相比。
- **滞后指标**：构建开始后的需求返工。统计同一变更在首次提交 `plan.md` 之后的所有 `spec.md` 提交次数。Git 日志会直接给出这一信息。

## 03 构建（Build）

没有既定的计划，任何措施都无法实施。机构知识转化为人工智能代理读取的文件，而安全防护措施则以代码的形式运行，而非习惯的形式存在。

### Claude Code 计划模式作为默认起点

工程师们以[计划模式](https://code.claude.com/docs/en/permission-modes)启动 Claude Code 会话，将第二阶段：设计阶段批准的 `spec.md` 交给 Claude，然后让 Claude 对他们进行面试，不断迭代计划，直到工程师满意为止。

> **传统方式**：工程师阅读设计图后开始编写代码。至于如何进行更改，细致到修改哪些文件和测试用例，都只存在于工程师的脑海中，或者最多只是在工单中留下一条注释。其他人无法进行审查。审查人员首先看到的是最终的差异对比，而到那时，返工的速度已经非常缓慢了。
>
> **AI 原生方式**：工作始于 Claude 在计划模式下生成的书面计划，该模式下它可以读取代码库而无需进行任何更改。工程师在编写代码之前对计划进行修正，最终提交的版本被确认为 `plan.md`，供后续阶段进行检查。

**入门**：

- **先决条件**：意图工件（`intent.md` 或 `spec.md`）如果存在的话；有 `CLAUDE.md` 文件也有帮助。
- **基础设施**：拥有代码库访问权限的 Claude Code。

**如何执行**：

1. 工程师以计划模式与 Claude 开始会话。
2. 工程师将 `intent.md` 和 `spec.md` 交给 Claude，要求给出实施计划，列出要更改的文件、工作顺序以及证明更改的测试。
3. 通过询问以下问题来审视该计划：这种改变可能会破坏什么，哪一步风险最大，以及 Claude 选择不做的其他哪些选项。
4. 反复迭代，直到即使是从未看过对话的工程师也能仅凭计划就实现变更。
5. 将已批准的计划提交为 `plan.md`。该计划将加入审计跟踪，PR 审查流程（阶段 5：部署）将检查最终差异是否与该计划相符。
6. 接受计划，让 Claude 去实现。有了扎实的计划，实现通常一次就能完成。
7. 当实现与计划出现偏差时，在同一次提交中更新 `plan.md`。可以考虑使用钩子来强制两者保持同步。

**长什么样（plan.md）**：

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)

## Files that change

portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py

## Order of work

1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.

## Risks

The claims-core API rate-limits at 50 rps; the panel must cache.

## Proof

test_status.py covers the four claim states; screenshot matches the
approved mock.
```

**治理方面的考虑**：设计评审发生在代码生成之前，此时更改方案只需编辑文档即可。计划模式本身就强制执行此流程，因为在工程师接受计划之前，Claude 无法编辑文件。计划及其修订版本以及接受者都会被记录在案。常规变更由工程师批准，而任何被组织视为高风险的变更都会提交给技术主管或架构师。

**如何测量**：

- **领先指标**：首次实现即合并的变更所占份额，以及从计划批准到合并 PR 的时间，所需数据都在 PR 元数据中。
- **滞后指标**：每次更改的返工周期，同样来自 PR 元数据；以及合并后的差异仍与已提交的 `plan.md` 匹配的频率。

### Claude Code 自动模式

Claude Code 也可以在自动模式下运行：工程师批准计划后，经过反复迭代，Claude 会自动应用每次更改，无需每次编辑都进行提示。随着后续剧本中的防护措施逐渐成熟（经过调优的 `CLAUDE.md`、编码策略的技能、阻止不安全操作的钩子以及 Claude 可以运行的测试套件），自动接受将成为日常工作的默认设置：严格的 `spec.md`、较小的影响范围以及测试已经覆盖的代码。

现在，用户不再是观看人工智能代理进行编辑和审核操作，而是在更长时间的自主会话后审核成果。自动接受模式与工作树结合使用时，能够进一步实现个人和团队之间的并行工作，这对于自主运行软件开发生命周期 (SDLC) 以及如第六阶段：维护中所述的闭环至关重要。

### 遗留系统和数据源（侧边栏）

适用于该过程产生的每个产物。

现有的软件开发生命周期（SDLC）流程可能已经跟踪了各种工件，只是并非以 Markdown 文件的形式记录。工作项可能存储在 Jira 中，需求可能存储在内置监管追溯功能的工具中，设计文档可能存储在 Figma 中，变更审批则可能通过变更看板进行。这些系统难以被取代，因为审计人员和监管机构已经认可它们，其他团队也依赖于它们，因此，AI 原生的 SDLC 必须适应现有系统。

在向 AI 原生软件开发生命周期 (SDLC) 过渡时，对于流程生成的每个工件，指定一个系统作为数据源（source of truth），其他所有系统都保存原始数据的副本或链接。以下配置可以设置为只有一个数据源，每个工件的数据源选择可能不同：

- **代码仓库作为权威数据源**。Markdown 文件是最终记录，而旧系统则引用提交中的文件。对于以工程为主导的组织而言，这可能是最简洁的配置之一，因为所有记录都集中在一个工具中，并由同一个时间戳作为权威依据。
- **旧系统作为数据源**。Jira、ServiceNow 或需求工具保存着权威记录，而 Markdown 文档则是工作副本。Claude 在会话开始时读取记录，并在生成规范或计划的同一会话中，通过 MCP 连接器将结果写回系统。
- **链接是最低要求**。所有工件都记录了记录 ID，所有旧记录都包含 Markdown 文件的提交 SHA 值。在向 AI 原生软件开发生命周期 (SDLC) 过渡时，链接是一个很好的起点，它意味着要接受存在两个数据源的事实。

旧系统和 Markdown 优先系统可以共存，只要两者之间存在联系，或者其中一个被声明为数据源。

### CLAUDE.md

[`CLAUDE.md`](https://code.claude.com/docs/en/memory) 为 Claude 提供一名新入职成员所需的背景知识，涵盖约定、命令、架构以及团队最常遇到的错误。过去存在于团队成员脑子里和维基百科上的知识，现在变成了一个文件，人工智能代理会在每次会话开始时阅读该文件，该文件由整个团队维护，并在出现错误时进行迭代更新。

**入门**：

- **先决条件**：没有任何。
- **基础设施**：一个代码仓库，已安装 Claude Code，以及一位熟悉代码库的工程师。

**如何执行**：

1. 在代码仓库中运行 `/init`。Claude 会根据找到的内容生成一个初始的 `CLAUDE.md`。
2. 将生成的文件精简到新员工入职第一天所需的大小。保留构建、测试和代码检查命令、重要的规范以及 Claude 经常出错的地方。
3. 将 `CLAUDE.md` 提交到仓库根目录的 Git 中，这样整个团队就共享同一个版本，并且可以像代码一样审查更改。
4. 这里有一条工作规则：当 Claude 两次犯下同一个错误时，就把更正写进 `CLAUDE.md`。
5. 尽量控制在一页以内，因为 Claude 会在每次会话开始时阅读全部内容，任何过时的内容都会白白占用上下文。

**长什么样（CLAUDE.md）**：

```markdown
# Payments service

## Commands

- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)

## Conventions

- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
- Every endpoint needs an integration test in src/itest.

## Architecture

- api/ holds REST controllers, core/ holds domain logic,
  adapters/ talks to external systems.
- Kafka events are defined in schemas/; never edit generated classes.

## Things Claude gets wrong

- Do not bump dependency versions; the platform team owns them.
- The legacy v1/ package is frozen; changes go in v2/.
```

**治理方面的考虑**：`CLAUDE.md` 采用版本控制，因此人工智能代理执行的指令可审查和审计。团队规范通过该文件应用，对其的更改会记录在 Git 历史记录中，代码所有者在 PR 审查中批准这些更改。

**如何测量**：

- **领先指标**：Claude 重复犯下本应由 `CLAUDE.md` 避免的错误的频率。对 `CLAUDE.md` 的更正或修改应该能在 Git 历史记录中被跟踪到。
- **滞后指标**：团队新成员合并第一个 PR 所需的时间（来自 PR 历史记录）。

### 技能即机构知识

[技能](https://code.claude.com/docs/en/skills)是组织把机构知识变成可操作工具的方式。这些技能的指令明确、版本可控、应用范围广，并在政策变更时集中更新。经验法则是：为必须始终如一应用的机构知识编写技能；不要为属于 `CLAUDE.md` 或提示组成部分的内容编写技能。

**入门**：

- **先决条件**：无需任何前提。有一个代码库和 `CLAUDE.md` 会有帮助，因为它能把人工智能代理的工作知识保存在仓库中，但技能并不依赖于此。
- **基础设施**：一项有指定所有者、且有书面权威依据的政策。

**如何执行**：

1. 选一项目前执行不一致的知识。这可以是安全标准、API 设计规范或品牌规则。
2. 将其编写成一项技能——一个包含 `SKILL.md` 的文件夹，其 frontmatter 说明触发时机，正文说明执行内容。工程师根据政策所有者的权威依据编写此技能，并借助 Claude 工具进行辅助。
3. 将该技能放在代码库的 `.claude/skills/<name>/` 下，使其随代码一起发布，或者通过[插件](https://code.claude.com/docs/en/plugin-marketplaces)在整个组织内分发。
4. 测试该技能是否被触发。让 Claude 以不同的方式完成相关任务，并确认每次技能都能被加载。
5. 当政策发生变更时，更改技能条款，并让政策所有者签署变更确认书。
6. 工程师在下次会话中会自动更新到新版本。

**长什么样（.claude/skills/secure-api-review/SKILL.md）**：

```markdown
---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
  modifying an external-facing endpoint, reviewing API code, or
  generating an OpenAPI spec.
---

# Secure API review

When you create or change an API endpoint:

1. Authentication: every endpoint requires the gateway JWT;
   no anonymous routes outside /health.
2. Input validation: validate request bodies against the OpenAPI
   schema and reject unknown fields.
3. Audit: every state-changing endpoint emits an audit event with
   actor, action, entity and timestamp.
4. Data classification: fields tagged pii in the schema must never
   appear in logs or error messages.

Run scripts/check-endpoints.sh and include its output in your summary.
```

**治理方面的考虑**：技能是一种控制手段，但属于建议性的。它使 Claude 在编写代码时更有可能应用该策略，但没有任何机制强制会话必须遵守该策略。一项必须始终有效的策略需要在技能背后有确定性的机制支撑，例如阻止操作的钩子或在 PR 中重新检查策略的审查流程。技能使违规情况变得罕见，而钩子则使违规几乎不可能发生。技能调用会被记录在会话跟踪中，政策所有者会像审查代码一样审查技能变更。

**如何测量**：

- **领先指标**：从政策所有者批准政策变更到更新后的技能合并的时间，取自技能文件夹上的 PR。
- **滞后指标**：PR 审查中引用该政策的发现数量，一旦技能在代码编写过程中应用了该政策，该数量应趋近于零。如果没有趋近于零，则说明该技能未触发，或者其文本与官方政策有所偏差。

### 钩子作为构建时的护栏

技能是一种建议性控制手段，而[钩子](https://code.claude.com/docs/en/hooks)则是其背后的确定性层。在实现过程中，Claude 的大部分操作都是文件编辑和 shell 命令，因此构建阶段是钩子触发最频繁的阶段。

构建阶段钩子可以：

- 阻止对受保护路径（例如生成的类或冻结的包）的编辑；
- 文件编辑后运行格式化程序和代码检查程序，以防止文件偏差累积；
- 将凭据从差异中排除。

为任何必须无一例外执行的策略配置钩子支撑。钩子会在每个匹配的操作上运行，因此构建阶段的钩子应该快速且作用域限定于已更改的文件。更繁重的检查（例如完整的测试套件）应该放在提交或 PR 环节。

请求人工批准的钩子应该放在第 5 阶段：部署的关卡中，因为在构建过程中发出批准提示会将人重新置于所有并行运行的会话的关键路径上。

### 并行会话和子代理

一名工程师可以同时驱动多个工作流。

- **并行会话**是另一个完整的 Claude Code 实例，它在自己的 [Git 工作树](https://code.claude.com/docs/en/worktrees)中执行独立的任务。每个独立的会话彼此互不了解，它们之间唯一的共同点是共同管理它们的工程师。
- **[子代理](https://code.claude.com/docs/en/sub-agents)** 在单个会话中作为作用域辅助程序运行，具有自己的上下文窗口和工具限制，适合在多个任务中重复执行的工作，例如验证应用程序是否按预期运行。

并行会话增加了工程师可以同时处理的任务数量，而子代理则确保每个会话专注于自身的任务。工程师的工作是统筹和审查所有这些会话。

> **传统方式**：一名工程师一次只处理一项任务，每天或每周的大部分时间都花在构建、测试和审核上。虽然可以在等待期间切换任务，但这种切换非常耗费精力，因此很少有人会选择这样做。
>
> **AI 原生方式**：一位工程师同时运行多个 Claude 会话，每个会话都在各自的工作树中执行各自的任务。重复执行的任务会变成子代理，拥有各自的上下文和工具限制。工程师的工作重心逐渐转移到协调，最终发展到构建和监控循环。

**入门**：

- **先决条件**：`CLAUDE.md`，因为所有会话都会读取该文件。反馈回路（阶段 4：测试）在这里也有帮助，因为当会话能够验证自身工作时，工程师所需的监督就减少了。
- **基础设施**：一个 git 仓库，因为隔离来自工作树；权限设置要调优到会话不会因为组织认为安全的命令而等待批准提示。

**如何执行**：

1. 工程师将工作拆分成涉及不同文件的任务，并参考计划模式剧本（阶段 3：构建）中的计划来确定哪些工作是独立的。共享文件的任务会在同一会话中依次运行。
2. 每个并行任务都有自己的工作树，例如 `claude --worktree feature-auth` 在一个终端中运行，而 `claude --worktree fix-rate-limit` 在另一个终端中运行。工作树是对其自身分支的独立检出，这可以避免会话之间在文件上发生冲突。
3. 两到三个会话是一个合理的起点。实际的上限取决于一个人能有效审查多少条工作流，所以只有在审查跟得上的情况下才增加会话。
4. 将重复性任务转换为子代理，每个子代理在 `.claude/agents/` 中的 Markdown 文件里定义，包含名称、使用场景描述以及可能涉及的工具。例如，代码简化器会在主代理完成后去除不必要的复杂性；验证器会运行应用程序并检查其行为；研究员会探索代码库并生成报告，而不会淹没主上下文。将这些定义提交到 Git，以便整个团队共享。

**长什么样（.claude/agents/verifier.md）**：

```markdown
---
name: verifier
description: Runs the app and checks the change works before the session
  reports done
tools: Bash, Read
---

Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

**治理方面的考虑**：会话越多，输出就越多，因此控制必须来自代码仓库中的配置。那里的钩子和权限设置适用于所有会话，会话的操作都会被记录并归因于运行该会话的工程师。

**如何测量**：

- **领先指标**：在审查质量不下降的前提下，每位工程师的并发会话数（从 OpenTelemetry 导出数据中统计），以及一天中用于指挥而不是等待的时间比例。
- **滞后指标**：根据 PR 历史记录确定的每周每位工程师合并的变更数，以及返工率。

## 04 测试（Test）

每个会话都会在人看到之前检查自己的工作，并且控制人工智能代理的配置会像它编写的代码一样进行回归测试。

### 给 Claude 一个反馈回路

始终为 Claude 提供验证自身工作的方法，无论是测试、构建还是屏幕截图差异。会话会在工程师发现问题之前检查自身工作并修复错误。

反馈回路不应与验证子代理（阶段 3：构建）混淆。反馈回路会在整个任务过程中随工作量反复运行。而验证子代理则提供了一种打包最终检查的方法：一旦会话认为工作已完成，就用一个新的上下文窗口运行检查。这样，最终结论就不会受到生成代码时所基于的假设的影响。

> **传统方式**：代码运行正常的信号到达得晚。持续集成（CI）系统几分钟后才能确认，测试人员几天后才能确认，生产环境则需要几周时间。如果代码是由人工智能代理生成的，那么信号延迟意味着需要有人检查所有输出，而这个人就成了瓶颈。
>
> **AI 原生方式**：会话在其他人看到结果之前，先获得检查自身工作的方法。运行测试、运行构建、截图。Claude 会不断迭代，直到检查通过为止，因此工程师看到的版本已经通过了检查。搭建这个回路的任务由运行会话的工程师负责，以下步骤正是为他们编写的。

**入门**：

- **先决条件**：没有任何。
- **基础设施**：一个测试套件和一个构建，各自只需一条命令即可在本地运行。对于 UI 工作，Claude 需要能够查看结果，这可以通过浏览器工具或通过 MCP 集成的截图工具来实现。

**如何执行**：

1. 如果今天检查工作需要一系列命令和一些环境知识，请将其包装在一个目标中，例如 `make test` 或 `npm test`，该目标在失败时返回非零值。
2. 在 `CLAUDE.md` 的「命令（Commands）」部分，列出每个命令并给出正常输出的示例。
3. 设定一个目标，并使其可量化，以便 Claude 无需询问即可检查工作，例如：「test_status.py 中的所有测试均通过」「屏幕截图与所附模拟稿匹配」或「端点使用新字段返回 200」。
4. 对于 bug 修复，首先要编写导致 bug 的测试用例。请 Claude 将该 bug 复现为测试，运行它，并确认其失败原因与预期一致。提交该测试。之后，再请 Claude 在不修改测试的情况下使其通过，并用最后一步提到的测试文件钩子来强制执行这一限制。一个在修复前就已存在、且人工智能代理无法重写的测试，就是 bug 已修复的证明。
5. 对于 UI 工作，用视觉检查来闭环。给 Claude 一个浏览器或截图工具，把模拟稿交给它，然后让它迭代。实现、截图、对比、调整。两到三轮迭代是正常的，每一轮的结果都应该有所改进。
6. 让验证成为「完成」定义的一部分。指令写在 `CLAUDE.md` 中：在报告任务完成之前运行测试，并展示输出。
7. 最后，回路本身也需要保护，因为修复代码的人工智能代理绝不能削弱对该代码的检查。可以通过一个钩子来阻止在修复任务期间对测试文件的编辑，从而实现这一点。另一种方法是在代码审查阶段检查差异，并拒绝任何涉及测试的更改。

**长什么样（CLAUDE.md 验证块）**：

```markdown
## Verifying your work

- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)

Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

**治理方面的考虑**：

- **强制执行的是什么**：在报告任务完成之前进行验证，以及在修复期间阻止人工智能代理编辑测试文件——在组织希望获得保证的地方，这两项都实现为钩子。
- **证据是什么**：「make test」的实际输出、构建日志或 Claude 运行并粘贴的屏幕截图差异，因此证据来自工具链。
- **记录位置**：在会话记录中（OpenTelemetry 导出会将其转发到组织的可观测性堆栈），以及在 PR 的检查运行中——审阅者和任何后续审计员都可以看到。
- **谁批准的**：审查 PR 的代码所有者，由于机械性的证据已经附上，他们可以专注于意图和风险。

**如何测量**：

- **领先指标**：人工智能代理编写的变更的首次 CI 通过率（CI 系统本身已支持）。
- **滞后指标**：每个 PR 的审查时间（来自 PR 元数据），一旦测试能够发现审查员过去发现的问题，审查时间应该就会下降；以及来自事件跟踪器的变更失败率。

### CI 中的持续评估

评估（eval）是 AI 领域中与阶段式质量保证（stage-gate QA）相对应的机制。实际上，这意味着每当人工智能代理的配置发生更改时，都会运行一套评估套件。当替换为新模型或重写提示时，评估套件会判断人工智能代理是否仍然能够以相同的标准完成工作。

评估应该被视为一个持续更新的套件。随着模型的改进，曾经能够区分的案例将不再有效，并且必须添加持续监测中出现的新案例。

根据具体使用场景，一些团队可能更倾向于按固定频率离线运行这些评估，而不是每次变更都评估。以下步骤适用于持续评估。

**入门**：

- **先决条件**：`CLAUDE.md` 和反馈回路（阶段 4：测试）。
- **基础设施**：能够以非交互方式运行 Claude Code 的 CI，以及用于评估运行的预算 API 密钥。

**如何执行**：

1. 平台工程师从最近的工作中收集 20 到 50 个真实任务及其预期/接受的结果。
2. 将每个任务写成一个评估，即提示加上定义可接受性的检查（测试通过、lint 干净、行为未改变、遵循策略）。
3. 该测试套件在 CI 中按计划以非交互方式运行，并且在 `CLAUDE.md`、技能或钩子发生任何更改时都会运行，因为这些配置控制着人工智能代理，理应获得与代码同等的回归测试。
4. 根据结果对配置变更设门。任何导致通过率下降的技能变更都会在合并前接受审核。
5. 每个生产事故都会得到一份评估，由负责该事故的团队编写，并作为回归测试保留在测试套件中。

**长什么样（.github/workflows/agent-evals.yml）**：

```yaml
name: Agent evals
on:
  pull_request:
    paths: ['CLAUDE.md', '.claude/**']
  schedule:
    - cron: '0 2 * * *'
jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - name: Run eval suite
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for eval in evals/*.json; do
            claude -p "$(jq -r '.prompt' $eval)" \
              --allowedTools "Read,Edit,Bash(make test)" \
              --output-format json > result.json
            ./evals/check.sh "$eval" result.json
          done
```

**治理方面的考虑**：评估为质量保证部门提供了一个跟得上人工智能代理输出节奏的门。通过率阈值通过合并检查来强制执行，运行过程会被记录以便进行长期结果比较，并且由负责配置变更的团队进行审批。

**如何测量**：

- **领先指标**：该套件每次运行都会报告评估通过率随时间的变化情况，以及生产事故需要多长时间才能变成永久性评估。
- **滞后指标**：CI 中捕获的回归与从事件跟踪器中发现的生产环境中的回归进行对比。

## 05 部署（Deploy）

审查是双向的，治理在人工智能代理执行过程中得到落实。人工智能代理负责生产门之前的所有操作，但不会越过生产门。

### AI 进入 PR 审核循环

Claude 既能给出审核意见，也能接收审核意见。它会根据组织政策审核收到的 PR，并处理自身 PR 上的审核评论。这使得工程师在审核 PR 时能够专注于行为本身，也就是判断意图和风险。

> **传统方式**：审稿能力是根据人工审阅量来规划的。PR 需要等待审阅者阅读全文，审阅质量会随着审阅者的工作量而波动，而作者则疲于应对不断增长的积压稿件。
>
> **AI 原生方式**：所有 PR 都会经过一套相同的审核流程，审核结果按严重程度排序。之后，审核的重点会提升到更高的层次，即变更是否达到了计划预期效果以及风险是否可接受。

**入门**：

- **先决条件**：来自阶段 3：构建的更新版 `CLAUDE.md`；如果审查流程需要执行书面政策，还需要技能和定义好的子代理。
- **基础设施**：一个已安装 Claude 集成的代码仓库，可以是管理员启用的托管式[代码审查](https://code.claude.com/docs/en/code-review)（研究预览版）服务，也可以是运行在您自己的 CI 环境中的 [claude-code-action](https://code.claude.com/docs/en/github-actions)，并根据需要通过 AWS Bedrock、Google Vertex 或 Microsoft Foundry 进行模型调用（CI/CD 流程涵盖了部署选项）。此外，需要代码所有者批准的分支保护策略也值得考虑。

**如何执行**：

1. 托管式代码审查服务是快速入门的选择。管理员只需启用该服务并选择代码仓库即可。如果您需要控制流水线或希望通过您自己的云协议路由 API 调用（CI/CD 流程已涵盖这些底层架构），则可以使用 claude-code-action 在您自己的 CI 环境中运行审查。
2. 技术负责人编写代码审查策略，将其作为 `REVIEW.md` 放在代码库根目录，并根据组织关注的审查流程进行划分：缺陷和逻辑错误；安全性和漏洞；是否符合规范（来自需求剧本的 `spec.md`）、实施计划（来自计划模式剧本的 `plan.md`）和设计原则。此外，`REVIEW.md` 还定义了哪些属于「重要（Important）」问题、哪些属于「小问题（Nit）」，以及哪些内容可以跳过。
3. 技术负责人设定人工审核阈值。审查发现本身并不会自动批准或阻止 PR，分支保护仍然需要代码所有者的批准。希望根据审查发现来阻止合并的平台工程师可以查看检查运行发布的机器可读计数，其中包含严重性计数。
4. 当审阅者或作者在审查评论中标注 `@claude` 时，Claude 会处理该评论并推送修复。PR 线程会记录请求和更改。此修复循环通过 claude-code-action 执行。在托管服务中，评论 `@claude review` 会请求一次新的审查。对于 Claude 创建的 PR，可以更进一步让 Claude 照看 PR 直到合并。团队会将此循环封装在一个自定义斜杠命令中，该命令会扫描 PR 中未解决的审阅评论和失败的检查，处理它们并推送修复，直到 PR 状态为绿色，仅等待代码所有者批准。
5. 审查发现会反馈到 `CLAUDE.md` 中。当审查第二次标记出同一个错误时，更正会作为该次审查的一部分提交到 `CLAUDE.md`；由于审查会读取 `CLAUDE.md`，这个错误从下一个 PR 开始就会被拦住。审查还会标记出哪些变更使 `CLAUDE.md` 变得过时。
6. 技术负责人每月根据审查发现对设置进行调优：给发现评分让审查器不断改进，并在 `REVIEW.md` 中限制 Nit 的数量。生成的路径以及 CI 已强制执行的任何内容都被排除在外。

**长什么样（REVIEW.md）**：

```markdown
# Review instructions

## Passes

Run three passes and tag each finding with its pass:

- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles

## What Important means here

Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.

## Cap the nits

Report at most five nits per review; summarize the rest as a count.

## Do not report

Generated files under src/gen/ and anything CI already enforces.
```

**治理方面的考虑**：职责分离得以维持，因为编写代码的人工智能代理无权审批代码。审查策略 `REVIEW.md` 适用于所有 PR，发现的问题、修复、评级和批准都会记录在 PR 历史记录中，因此 PR 本身就是审计记录。最终的批准由人工通过分支保护机制进行，并参考审查发现。

有关这些控制措施如何在生产规模上组合，请参阅 Anthropic 的[「确保 AI 原生 SDLC」](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)。

**如何测量**：

- **领先指标**：首次审查时间（应该降到分钟级），以及无需人工动分支就解决掉的审查评论所占比例，数据直接存储在 Git 上。
- **滞后指标**：从 PR 历史记录和事件跟踪器中，将合并前发现的缺陷和漏洞与逃逸到生产环境中的缺陷和漏洞进行对比。

### 钩子作为审批门

构建阶段使用钩子作为安全屏障，允许或阻止无需人工干预的操作（阶段 3：构建）。钩子还可以发出请求，暂停操作直到特定人员批准，这正是发布门控机制所需要的。

该剧本位于第五阶段：部署，因为发布门控是最清晰的案例，但钩子并非部署专属：它们会在 Claude 执行任何操作时运行。例如，在第三阶段：构建期间，钩子可以阻止在没有变更单的情况下对迁移和基础架构进行编辑；在第四阶段：测试期间，钩子可以阻止人工智能代理在修复任务中编辑测试文件。

**入门**：

- **先决条件**：没有任何。
- **基础设施**：变更流程所需审批的书面清单。

**如何执行**：

1. 工程领导层，包括变更管理和合规部门，列出必须保留的人工审批关卡，例如变更管理签字、发布授权和对受保护路径的编辑。
2. 平台工程师将每个门都表示为一个钩子——一个在 Claude 执行操作之前运行的脚本，可以允许、询问或阻止。
3. 团队钩子放在 git 中的 `.claude/settings.json` 里，不可协商的钩子放在平台或 IT 管理员拥有的托管设置中，个人工程师无法将其关闭。
4. 阻止动作应该能够自我解释：当钩子拦截一个动作时，原因和审批路径会出现在 Claude 的输出中。

**长什么样（.claude/settings.json）**：

```json
{
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Bash",
          "hooks": [
            { "type": "command",
              "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh" }
          ]
        }
      ]
    }
}
```

以及网关本身（`.claude/hooks/production-gate.sh`）：

```bash
#!/bin/bash

# Production deploys require a named release authorization

cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
   if [ -z "$RELEASE_APPROVAL" ]; then
     echo "Production deploys need a release authorization." >&2
     exit 2 # exit 2 blocks the action; the message goes to Claude
   fi
fi
exit 0
```

**治理方面的考虑**：钩子是审批门。门条件每次都会对所有人强制执行。允许和阻止的决定都会被记录并带有时间戳。门还定义了什么才算作批准，无论是已批准的变更单还是发布经理的签字。

**如何测量（针对钩子本身）**：

- **领先指标**：每个审批门的等待时间。每个钩子操作的决定都会连同时间戳和允许或阻止的判定结果一起写入 OpenTelemetry 导出文件中，因此每个审批门的等待时间都是可见的。
- **滞后指标**：事件跟踪器中，门禁违规事件在安装钩子前后进入生产环境的情况。

### 受监管企业的托管设置（示例）

由平台团队通过 MDM 或管理控制台部署；工程师无法编辑或覆盖任何内容。

```json
{
  "permissions": {
    "deny": [
      "Read(.env*)", "Read(./secrets/**)",
      "WebFetch", "Bash(curl *)", "Bash(wget *)"
    ],
    "allow": [
      "Bash(git *)", "Bash(make build)",
      "Bash(make test)", "Bash(make lint)"
    ],
    "disableBypassPermissionsMode": "disable"
  },
  "allowManagedPermissionRulesOnly": true,
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "network": { "allowedDomains": ["git.internal.example.com",
                  "registry.npmjs.org"] },
    "credentials": {
      "files": [
        { "path": "~/.ssh", "mode": "deny" },
        { "path": "~/.aws/credentials", "mode": "deny" }
      ],
      "envVars": [ { "name": "GITHUB_TOKEN", "mode": "deny" } ]
    }
  },
  "allowManagedHooksOnly": true,
  "disableSideloadFlags": true,
  "allowManagedMcpServersOnly": true,
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "example-corp/approved-plugins" }
  ],
  "requiredMinimumVersion": "2.1.193"
}
```

从控制角度看，每一行配置买到了什么：

- `permissions.deny` 将秘密信息隔离在人工智能代理的上下文之外，并通过工具阻止任意网络出口；`permissions.allow` 预先批准安全的内部循环，避免拒绝列表导致提示疲劳。
- `disableBypassPermissionsMode` 加上 `allowManagedPermissionRulesOnly` 意味着任何工程师、项目文件或命令行标志都不能扩大规则范围。
- `sandbox` 弥补了权限无法弥补的缺陷。在 WebFetch 上使用工具级拒绝规则并不能阻止 shell 命令访问网络；操作系统级别的域允许列表会直接阻止出站流量。
- `failIfUnavailable` 和 `allowUnsandboxedCommands` 使沙箱成为门禁：当沙箱无法初始化时，Claude Code 拒绝启动；在沙箱内部失败的命令无法在沙箱外部重试。
- `credentials` 弥补了拒绝规则留下的漏洞。`permissions.deny` 管理着 Claude 的文件工具，但默认情况下，沙盒化的 shell 命令仍然可以读取 `~/.ssh` 或 `~/.aws/credentials`；此代码块拒绝这些读取操作，并从每个沙盒化命令的环境中剥离指定的密钥。
- `allowManagedHooksOnly` 意味着来自本剧本的审批门是唯一运行的钩子；任何本地内容都不能添加或替换它们。
- `disableSideloadFlags` 和 `strictKnownMarketplaces` 意味着工程师机器上的每个技能、人工智能代理、钩子和 MCP 服务器都是通过组织批准的插件市场获得的，而不是来自主目录。
- `allowManagedMcpServersOnly` 使人工智能代理的工具面板成为平台团队拥有的允许列表。
- `requiredMinimumVersion` 拒绝从低于批准下限的版本启动，因此控制措施由组织实际评估过的版本来执行。

以上配置请当作一个起点来定制，而不是照搬的推荐。任何拒绝操作都会影响功能，而合适的平衡点取决于代码库的数据分类。设置参考文档记录了所有键值，包括仅供托管使用的键值：[code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings)。

### CI/CD 集成与部署

在 CI/CD 管道内以非交互方式运行 Claude Code，对执行进行沙箱化，以便长时间运行的人工智能代理能够安全运行，通过 [MCP](https://code.claude.com/docs/en/mcp) 集成公开部署，并在人工智能代理需要回滚路径之前对其进行演练。

> **传统方式**：流水线运行确定性脚本，任何需要人工判断的事情都由人工处理。例如，对不稳定的测试进行优先级排序、编写变更日志或找出构建失败的原因。部署和回滚则是人工在压力下遵循的运行手册。
>
> **AI 原生方式**：Claude 在流水线内部以非交互方式运行，用于执行判断步骤，运行环境为沙箱，并具有限定范围的凭据。部署工具通过 MCP 向人工智能代理公开，因此编写和测试变更的工作流也可以在组织为每个环境定义的权限范围内发布和回滚变更。

**入门**：

- **先决条件**：Claude 进入 PR 审核循环以及钩子作为审批门，因为在自动化加速任何操作之前，必须先存在这些门。
- **基础设施**：安装了 claude-code-action 的 CI 平台，或任何可以调用 `claude -p` 的运行器；通过 API 访问模型，或在流量必须留在组织云协议内时通过 Bedrock、Foundry 或 Vertex 访问；部署目标的 MCP 服务器；用于人工智能代理作业、不持有长期生产凭证的沙箱配置文件。

**如何执行**：

1. 平台工程师首先执行只读判断步骤。可以在流水线作业中使用 `claude -p` 对构建失败进行分类、总结不稳定的测试结果或撰写变更日志。
2. 在现有门禁之后添加写入步骤，用于执行诸如修复代码检查、更新生成的文档或通过 `@claude` 提及回复评审意见等任务。人工智能代理写入的任何内容都会通过分支保护以 PR 的形式提交，人工智能代理本身没有权限推送到主分支。
3. 沙盒化执行。人工智能代理作业在容器中运行，并遵循网络策略，使用有效期较短的作用域令牌，默认情况下不持有任何生产凭据。
4. 通过 MCP 公开部署。部署、状态和回滚都变成了工具，并按环境进行范围限定，因此人工智能代理的部署权限是一个允许列表，而不是一个带有凭据的 shell 脚本。
5. 根据环境对自主性进行分层。在开发环境中，人工智能代理可以自由部署。在生产环境中，人工智能代理准备发布版本，发布管理器进行授权，并通过钩子强制执行生产环境的发布门槛。预发布环境则介于两者之间。
6. 回滚应该是流水线中最常演练的路径，它是人工智能代理可以执行的单个命令，并在预发布环境中定期演练。闭环剧本（阶段 6：维护）会在控制带被突破时调用此回滚操作，因此必须事先进行验证。

**长什么样（流水线步骤）**：

```yaml
- name: Triage failed build
  if: failure()
  run: >
    claude -p "Read the build log at out/build.log. Identify the most
    likely cause, say whether the failure looks flaky or real, and write a
    three-line summary for the PR thread." >> triage.md
```

**治理方面的考虑**：其基本原则是：人工智能代理只能在生产门之前行事，而不能越过生产门。以下控制措施旨在确保这一原则得到落实。

- 分支保护会将人工智能代理编写的任何内容都变成 PR，而没有直接通往主分支的路径。
- 生产部署钩子会阻止发布，直到指定的发布经理授权为止。每次非交互式运行都以人工智能代理自身的身份运行，因此流水线日志会将人工智能代理执行的操作与触发该操作的工程师执行的操作区分开来。
- 每个环境的权限等级决定了人工智能代理在到达大门之前可以执行多少操作。

**如何测量**：

- **领先指标**：无需呼叫人工就能完成故障排查的流水线故障所占比例（取自 CI/CD 流水线日志）。
- **滞后指标**：DevOps 研究与评估 (DORA) 指标，CI 系统和部署工具已经在产出这些指标。

## 06 维护（Maintain）

循环闭合。触发器在调用路径中没有人的情况下调用 Claude，而它发现的内容以 `intent.md` 的形式重新进入流水线。

### 维护与闭环

到目前为止，我们已经讨论了如何将 Claude 添加到软件开发生命周期 (SDLC) 的每个阶段，每个阶段都需要人工启动初始步骤。然而，本阶段将重点转移到 Claude 的自主运行，从而形成闭环。

例如，持续运行的监控代理可以在缺陷单被提交后创建一个 `intent.md`，并按需求、计划、构建、测试和评审阶段流转。第六阶段：维护以无头模式运行，各阶段之间设有独立的置信度门，通过确定性检查或对抗性评审代理来决定上一阶段的输出是继续执行还是上报给人工处理。

> **传统方式**：维护是一个被动的过程。所有工单或事件都需要有人处理才能重新启动流程。凌晨 3 点触发的警报可能会被忽略，工单可能会一直积压在待办事项列表中，直到有人处理，而如果另一个问题先发生，事后采取的措施可能根本无法应用到代码库中。
>
> **AI 原生方式**：当出现控制带故障、工单、频道消息或日程安排等触发事件时，无需人工干预，Claude 即可自动启动。Claude 会进行诊断，仅通过预设的受门禁路径执行操作，并将诊断结果记录为 `intent.md`，然后按照上述阶段流转。人工负责对这些工作进行分类和审核，无需再从头开始。

### 闭环

一个确定性脚本会监控生产过程，并在控制带被突破时调用 Claude。监控阈值突破是循环自主运行模式的一个有用示例，而阶段末尾的 Claude Tag（公开测试版）部分则涵盖了通过不同渠道到达的工作。

**入门**：

- **先决条件**：`intent.md`——它给循环提供了一个结构化的输出以便重新启动；Claude 加速的 PR 审查、作为操作边界的钩子，以及 CI/CD 的回滚路径（最高自治层级会调用该路径）。
- **基础设施**：检测脚本可以查询的指标存储（Prometheus、CI 系统的 API 或等效项）；对仓库的读取访问权限；在 CI 中以非交互方式运行 Claude Code 的方法；或者用于接收 webhook 的服务的 [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)。

**如何执行**：

1. 服务所有者或平台工程师选择一个具有稳定滚动基线的指标，例如 CI 测试失败率、部署后 5xx 错误率或 PR 周期时间。
2. 他们编写检测脚本，通常对滚动窗口计算均值和标准差，并叠加规则（如 Western Electric 规则或类似规则），以便频带既能捕捉到缓慢的漂移，也能捕捉到尖峰信号。该脚本经过版本控制和单元测试，检测过程完全确定性，不涉及任何模型。
3. 响应层级在版本控制的配置中定义（`bands.yaml` 如下）。在 1σ 层级，脚本仅记录日志；在 2σ 层级，脚本会以只读方式调用 Claude 进行诊断；在 3σ 层级，Claude 可以执行操作，但只能通过向审查门提交 PR 或触发预先批准的运行手册来实现。
4. 触发层可以是 GitHub 或 GitLab 中的定时工作流、现有监控堆栈中的 Webhook，或是网络内部的 Cron 作业。Claude 以无状态方式运行，既可以作为 CI 运行器上的非交互式步骤，也可以作为沙盒容器中的 Agent SDK 服务。CI/CD 流程涵盖了部署和模型访问选项。由于运行是无状态且非交互式的，因此循环可以在无人启动的情况下开始和结束。
5. 人工智能代理按照第一阶段：计划的 `intent.md` 格式编写诊断报告，内容包括异常及其证据、拟议的解决方案、受影响的系统以及任何未解决的问题。之后，该诊断结果会像其他任何内容一样进入后续流程。
6. 服务负责人或值班工程师对队列进行分诊，并将与产品相关的发现转交给产品负责人。分类方式包括：立即修复、安排处理或忽略。忽略操作有助于调优频带，减少噪声。
7. 当修复发布时，为这次事件添加一个评估（持续评估剧本发挥作用），以确保此类问题今后受到保护。

**长什么样（例如，一个用于监控 CI 测试失败率的 bands.yaml 文件）**：

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose,
            tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose,
            routes: [pull_request, runbook:rollback-deploy] }
```

**治理方面的考虑**：层级边界通过版本控制的配置强制执行，权限和托管设置会阻止对生产环境的访问。调用、发现的问题和分诊决策都会被记录并带有时间戳。服务所有者负责分诊和批准发现的问题，由此产生的变更需要经过正常的 PR 审查门，人工智能代理可能触发的运行手册也已事先获得批准。

**如何测量**：

- **领先指标**：从控制带被突破到 `intent.md` 进入分诊队列的时间，对比过去从事件发生到事后分析措施的时间。检测脚本的日志包含故障时间戳和事件层级。
- **滞后指标**：成为已合并修复的发现所占比例（分诊队列对照实际 PR 历史记录），以及同一类别的重复事件——随着修复向评估套件添加案例，该比例应该会下降。

**示例**：

- 当 CI 测试失败率超过 3σ 时，人工智能代理会隔离不稳定的测试或打开回滚 PR，然后由审查门决定。
- 当部署窗口内的部署后 5xx 错误率超过 3σ 时，人工智能代理会触发现有的回滚管道。
- 当 PR 周期时间触发漂移规则时，人工智能代理会为工程领导编写一份报告——这表明该框架同样适用于流程指标和生产指标。
- 检测机制保持确定性。一旦某个频带被突破，Claude 就会被激活，其具体行动取决于频带层级。

### 定期代码库扫描

安全扫描是对特定模型下代码库在特定时间点的评估，但其结果会随着时间推移而过时：代码每周都在变化，而且每一代模型都会发现前一代遗漏的漏洞。AI 原生的解决方案是按计划运行扫描，调用路径中没有人工，并将发现的信息与代码库的任何其他变更一样，通过相同的门禁进行审核。

[Claude Security](https://claude.com/product/claude-security) 是定时扫描的托管形式。只需连接一个 GitHub 代码库，扫描即可在 Anthropic 的基础设施上运行，扫描过程使用 Claude Mythos 5 模型。每次扫描结果都会经过验证，并在报告前附上置信度评级。建议的补丁会在 Claude Code 网页版上进行审核和应用。组织无需访问模型本身即可获取扫描结果。

> **传统方式**：安全扫描是一个事件，在版本发布或审计之前启动。扫描报告会提交到跟踪系统，积压问题需要人工处理，直到下一次扫描事件开始。在此期间编写的代码只由 PR 审查中发现的问题所覆盖。
>
> **AI 原生方式**：扫描会按计划针对所有已连接的存储库运行，使用性能最强的可用模型，并在任何人阅读之前验证扫描结果。每个发现都按照控制带违规的处理方式处理：一个 PR 就能容纳的修复会通过审查门，任何更大的修复都会被记录为 `intent.md`。覆盖范围的日期以最近一次运行为准，而不是第一次运行。

**入门**：

- **先决条件**：PR 审查门和钩子作为审批门（阶段 5：部署），以便发现的问题能够像其他任何变更一样经过审查。用阶段 1：计划的 `intent.md` 格式记录单个 PR 无法容纳的发现。
- **基础设施**：Claude Security 目前以公开测试版的形式面向 Claude Enterprise 组织开放。它需要在目标代码库（云端托管的 github.com）上安装 Anthropic GitHub 应用，启用 Claude Code on the Web，开启额外使用量（Extra Usage）并设置消费限额，为执行扫描的用户配备高级席位，并且由管理员在 `claude.ai/admin-settings/claude-code` 处启用该功能。扫描按消费量以 Mythos 5 的费率计费，因此消费限额应与代码库的大小和数量相匹配。

**如何执行**：

1. 安全负责人将各个存储库连接起来，并按存储库、服务或团队将它们组织成项目，以便从一开始就明确发现结果的归属。
2. 首先对最重要的代码库进行一次全面扫描，包括之前已被其他工具或早期模型扫描过的代码库。将首次扫描结果作为基准。首次扫描可能会在之前被认为干净的代码中发现问题。
3. 为每个项目设定一个计划。对于正在积极开发的服务，每周一次是一个合理的默认值；如果代码库很大或内容混合，则将扫描范围限定在特定目录或分支上。
4. 根据置信度评级对发现结果进行分诊。排除某项发现时需说明理由，以便记录排除情况，避免下次运行时再次出现相同的结果。
5. 对于范围限定的发现，请在 Claude Code 网页版中打开建议的补丁，进行审查，然后像其他变更一样通过 PR 审查门提交。提出修复方案的人工智能代理无权批准该方案。
6. 对于比单个补丁更广泛的问题，例如架构缺陷或跨服务重复出现的模式，请按照第一阶段格式编写 `intent.md`，并从「计划」开始。
7. 当修复发布到生产环境时，从持续评估剧本中为该漏洞类别向评估套件添加一个评估，以便从那时起对控制人工智能代理的配置进行该类别的测试。
8. 将调查结果导出为 CSV 或 Markdown 格式，或使用 webhook，以保持组织现有的跟踪和审计系统作为记录系统，因为审计人员已经期望使用这些系统。

**治理方面的考虑**：扫描在组织的管理控制下运行，这意味着连接的存储库、扫描席位持有者以及消费限额均由组织集中设置。每项发现都包含验证结果和置信度评级，每项排除都有相应的理由，因此扫描历史记录是对已发现、已修复和已确认问题的审计记录。

修复通过 PR 审查门和分支保护机制而非扫描本身进入生产环境。Claude Security 增强了现有的静态分析和依赖项扫描。确定性检查保留在持续集成 (CI) 环境中，而模型驱动的扫描则覆盖了这些检查无法发现的上下文相关漏洞。

**如何测量**：

- **领先指标**：已接入计划的已连接存储库所占比例，以及从发现被报告到其补丁进入 PR 审查门的时间，从扫描历史记录和 PR 元数据中读取。
- **滞后指标**：将计划扫描发现的漏洞与生产环境中发现的漏洞或事件跟踪器中的外部报告进行对比；并分析已运行多次的存储库中每次扫描的发现趋势，随着修复和评估的积累，该趋势应该会下降。

### Claude 用 Claude Tag 值班

事件还可以通过其他渠道传入，例如工作场所的沟通应用，如 Slack 或 Teams。事件可能表现为晚上 10 点在 Slack 事件频道中收到的紧急修复消息，现在可以立即采取行动。Claude Tag（目前在 Slack 中提供公开测试版）使 Claude 以独立身份加入这些频道，因此每个新事件都会有第一个响应者，并且响应本身也会成为循环的一部分，供未来事件参考。

对话和机构知识都保留在频道内，频道中的任何成员都可以指导和推进响应。任何团队成员都可以测试假设、探索新方案并进行实时调查，频道历史记录增强了可审计性。通过访问 MCP，Claude 验证指标是否已恢复到基线水平，并在讨论串中确认，并将事后分析写入版本控制的经验教训文件，供未来的调查参考。

事件并不是 Claude Tag 承接的唯一工作。无论是通过 MCP 提交的工单还是在频道中提出的请求，Claude 都会以相同的方式进行分诊。小型、范围明确的修复会以 PR 的形式通过审查门，而任何较大的修复都会被记录为第一阶段：计划的 `intent.md`，此时循环便开始自我补给。参见：[Claude Tag 如何在 Anthropic 负责 CI/CD 的轮班值守](https://claude.com/blog/ai-ci-cd-on-call)。

![频道就是审计跟踪：请求、诊断、人工授权和修复都保留在事件处理的地方。](asset/img/claude-tag-channel.png)

## 结语

模型和框架变得更加先进，使组织不仅可以改变其代码生成方式，还可以改变整个软件开发生命周期。

这一转变使人的判断在过程中保持核心地位，并考虑了大型企业组织的治理和监管要求。

本指南汇总了我们应用 AI 团队每天为客户执行的许多真正最佳实践，我们希望您觉得它是一个实用且可操作的资源。

循环持续运转，人的判断始终在其之上。

### 资源与致谢

以下文档是平台团队搭建上述控制措施所需的资料，大致按部署顺序排列：

- [Set up Claude Code for your organization — the admin decision map; start here](https://code.claude.com/docs/en/admin-setup)
- [Settings reference and precedence, including every managed-only key](https://code.claude.com/docs/en/settings)
- [Server-managed settings from the Claude admin console](https://code.claude.com/docs/en/server-managed-settings)
- [Permissions](https://code.claude.com/docs/en/permissions)
- [Sandboxing — OS-level filesystem and network isolation](https://code.claude.com/docs/en/sandboxing)
- [Hooks — guide](https://code.claude.com/docs/en/hooks-guide)
- [Hooks — reference](https://code.claude.com/docs/en/hooks)
- [Skills](https://code.claude.com/docs/en/skills)
- [Plugins and private marketplaces — how skills and hooks are distributed organization-wide](https://code.claude.com/docs/en/plugin-marketplaces)
- [Managed MCP — central control of the agent&#39;s tool surface](https://code.claude.com/docs/en/managed-mcp)
- [Enterprise deployment overview — Bedrock, Vertex, Foundry](https://code.claude.com/docs/en/third-party-integrations)
- [Enterprise network configuration](https://code.claude.com/docs/en/network-config)
- [Monitoring (OpenTelemetry)](https://code.claude.com/docs/en/monitoring-usage)
- [The analytics dashboard](https://code.claude.com/docs/en/analytics)
- [Compliance API — Enterprise activity feed, chat retrieval and deletion](https://platform.claude.com/docs/en/manage-claude/compliance-api)
- [Security model](https://code.claude.com/docs/en/security)

感谢 Jim Blackhurst、Will Steuk 和 Jamal Arif 对本指南的贡献，本指南的灵感来源于并建立在他们此前大量工作的基础之上。
