# OpenClaw

## 安装

如果有nodejs，可以用npm 安装
```bash
npm install -g openClaw@latest
# 或
pnpm add -g openClawt@latest
```

### 引导向导

运行 openClaw onboard --install-daemon 配置

```bash
penClaw onboard --install-daemon
```
输出
Screen 1:
```text
│
◇  Security ──────────────────────────────────────────────────────────────────────────────╮
│                                                                                         │
│  Security warning — please read.                                                        │
│                                                                                         │
│  OpenClaw is a hobby project and still in beta. Expect sharp edges.                     │
│  This bot can read files and run actions if tools are enabled.                          │
│  A bad prompt can trick it into doing unsafe things.                                    │
│                                                                                         │
│  If you’re not comfortable with basic security and access control, don’t run OpenClaw.  │
│  Ask someone experienced to help before enabling tools or exposing it to the internet.  │
│                                                                                         │
│  Recommended baseline:                                                                  │
│  - Pairing/allowlists + mention gating.                                                 │
│  - Sandbox + least-privilege tools.                                                     │
│  - Keep secrets out of the agent’s reachable filesystem.                                │
│  - Use the strongest available model for any bot with tools or untrusted inboxes.       │
│                                                                                         │
│  Run regularly:                                                                         │
│  openclaw security audit --deep                                                         │
│  openclaw security audit --fix                                                          │
│                                                                                         │
│  Must read: https://docs.openclaw.ai/gateway/security                                   │
│                                                                                         │
├─────────────────────────────────────────────────────────────────────────────────────────╯
│
◆  I understand this is powerful and inherently risky. Continue?
│  ● Yes / ○ No
└
```
Screen 2:
```text
◇  I understand this is powerful and inherently risky. Continue?
│  Yes
│
◆  Onboarding mode
│  ● QuickStart (Configure details later via openclaw configure.)
│  ○ Manual
└

```





[openclaw github](https://github.com/openClaw/openClaw)
[openclaw book](https://www.openclawbook.xyz/readme-zh)
