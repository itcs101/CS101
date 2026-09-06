---
title: Microsoft Skill Recorder
---

# Microsoft Skill Recorder

[Skill Recorder](https://github.com/microsoft/skill-recorder) 是 Microsoft 开源的桌面工具，用来把一次真实的电脑操作记录下来，并转换成 AI Agent 可以重复执行的 Skill 或 Automation。

## 它解决什么问题

很多工作流程并不是一句提示词就能说明白的：操作者需要在多个应用之间切换、访问网页、填写表单、复制信息，再根据页面反馈做下一步。Skill Recorder 让用户先完整做一遍任务，再由 GitHub Copilot CLI 根据操作记录重建任务意图和有序步骤。

它适合沉淀以下类型的流程：

- 重复性的后台操作，例如录入数据、提交表单和生成报表
- 跨网页、桌面应用和命令行工具的工作流程
- 团队内部的标准操作流程和业务知识
- 需要定期执行的检查、整理和通知任务
- 将个人经验整理成 AI Agent 可以调用的操作能力

## 工作方式

1. **Record**：开始录制并完成一次任务。工具在本地捕获屏幕、应用窗口切换、浏览器 URL 和部分剪贴板预览，也可以选择录入语音讲解。
2. **Analyze**：任务完成后提交分析，由 GitHub Copilot 重建一个总体意图和按顺序排列的步骤。
3. **Review**：检查并编辑分析结果，确认步骤、目标和边界符合预期。
4. **Create**：将结果生成可复用的 `SKILL.md`，或者生成带触发条件和执行计划的 Automation。

生成的流程优先使用 Agent 的原生工具，例如 `gh` CLI 或 `web_fetch`，而不是机械地重复屏幕点击。因此，录制一次“提交某个表单”的示例，有机会泛化为“提交同类表单”的能力。

## 与普通屏幕录制的区别

Skill Recorder 的重点不是保存视频教程，而是从一次操作中提取：

- 任务的目标和意图
- 完成任务所需的步骤
- 每一步的输入、判断和结果
- 可以交给 Agent 执行的工具调用方式

最终产物是面向 Agent 的结构化 Skill 或自动化流程，而不是只能供人观看的视频。

## 安装与使用

项目目前以 source release 的形式发布。macOS 是主要目标平台，同时支持 Windows 11。安装时应从官方 [最新 Release](https://github.com/microsoft/skill-recorder/releases/latest) 获取对应平台的命令；每个 Release 使用固定 commit 构建，避免直接跟随不确定的源码状态。

使用前需要：

- GitHub 账号和 Copilot 使用权限
- macOS 的屏幕录制权限，或 Windows 11 环境
- 允许应用在本地记录屏幕和操作过程

基本流程是：安装并启动应用，点击 Record 完成任务，点击 Analyze 检查结果，最后创建 Skill 或 Automation。

## 隐私与安全

录制、存储、画面抽取和可选的语音转写默认在本机完成。只有用户点击 Analyze 后，操作时间线、窗口或文档标题、URL、剪贴板预览、抽取的屏幕图像和语音文本才会发送到 GitHub 云端供 Copilot 处理。

不要在录制过程中输入、复制、粘贴、展示或朗读以下信息：

- 密码和登录凭据
- API Key、访问令牌和私钥
- 客户数据、个人信息和其他机密内容

录制前应使用测试账号或脱敏数据，并在生成 Skill 后人工检查步骤中是否包含敏感信息。生成的 Skill 也应遵守最小权限原则，避免让 Agent 获得不必要的文件、网络或系统操作权限。

## 局限

- 录制结果仍需要人工审查，不能把一次成功执行视为完整的业务规则
- 页面布局、权限和数据变化可能导致录制出的步骤失效
- 涉及登录、验证码、审批和异常分支的流程通常需要额外补充规则
- Analyze 会把录制数据发送到 GitHub 云端，因此不适合直接录制机密业务流程
- 生成 Skill 后应补充失败处理、输入校验和幂等性要求

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/skill-recorder)
- [最新 Release](https://github.com/microsoft/skill-recorder/releases/latest)
- [MIT License](https://github.com/microsoft/skill-recorder/blob/main/LICENSE)
