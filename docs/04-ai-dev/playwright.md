---
title: Playwright
---

# Playwright

[Playwright](https://playwright.dev/) 是 Microsoft 开源的浏览器自动化与端到端测试框架，支持 Chromium、Firefox 和 WebKit，并提供 JavaScript/TypeScript、Python、Java 和 .NET API。

## 适合什么场景

- Web 应用端到端测试
- 跨浏览器回归测试
- 登录、表单、文件上传和下载流程验证
- 浏览器自动化和数据采集
- 截图、录屏、Trace 和失败现场留存
- 验证 AI Agent 的浏览器操作结果

## 核心能力

- 自动等待元素达到可操作状态，减少固定 sleep
- 使用 locator、role、text 和 label 定位页面元素
- Browser Context 提供相互隔离的会话环境
- 支持网络拦截、请求模拟和响应断言
- 支持截图、视频和 Trace Viewer
- 支持并行运行测试和多浏览器项目配置

## 基本流程

1. 启动浏览器或创建 Browser Context。
2. 打开页面并执行用户操作。
3. 断言页面、URL、网络响应或文件结果。
4. 测试结束后关闭上下文。
5. 失败时查看截图、视频和 Trace。

示例：

```ts
import { test, expect } from '@playwright/test';

test('user can sign in', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.getByLabel('Email').fill('user@example.com');
  await page.getByLabel('Password').fill('password');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
});
```

## 使用建议

- 优先使用语义定位器，不要依赖脆弱的 CSS 层级或自动生成 class。
- 每个测试创建独立的 Browser Context，避免测试之间共享状态。
- 用 API 或数据库准备测试数据，减少对 UI 登录流程的依赖。
- 对关键流程保存 Trace，方便复现失败现场。
- 在 CI 中固定浏览器版本、超时和重试策略。
- 测试应验证用户可观察行为，而不是页面内部实现细节。

## 局限与注意事项

Playwright 不能替代单元测试、API 测试和性能测试。端到端测试运行较慢，也更容易受到网络、浏览器版本和外部服务影响。测试账号、Cookie、Token 和用户数据不得写入仓库或录屏产物。

## 相关链接

- [Playwright 官方文档](https://playwright.dev/docs/intro)
- [Playwright GitHub](https://github.com/microsoft/playwright)
- [Trace Viewer](https://playwright.dev/docs/trace-viewer)
