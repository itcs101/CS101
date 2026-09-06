# 在Claude Code 中使用DeepSeek

1. 安装下面的指引设置终端参数
   https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code
2. 修改Claude Code 的配置文件

> 这里要点是配置的参数请与deepseek官方提供的一致

```json
"claudeCode.environmentVariables": [
           {
            "name": "ANTHROPIC_BASE_URL",
            "value": "https://api.deepseek.com/anthropic"
        },
        {
            "name": "ANTHROPIC_AUTH_TOKEN",
            "value": "sk-e9addcb5b8264aebb188438fe07c853f" //换上你自己申请的API 密钥*****************************************
        },
        {
            "name": "API_TIMEOUT_MS",
            "value": "600000"
        },
        {
            "name": "ANTHROPIC_MODEL",
            "value": "deepseek-v4-pro[1m]"
        },
        {
            "name": "ANTHROPIC_SMALL_FAST_MODEL",
            "value": "ddeepseek-v4-pro[1m]"
        },
        {
            "name": "ANTHROPIC_DEFAULT_OPUS_MODEL",
            "value": "deepseek-v4-pro[1m]"
        },
        {
            "name": "ANTHROPIC_DEFAULT_SONNET_MODEL",
            "value": "ddeepseek-v4-pro[1m]"
        },
        {
            "name": "ACLAUDE_CODE_SUBAGENT_MODEL",
            "value": "deepseek-v4-flash"
        },  
        {
            "name": "ANTHROPIC_DEFAULT_HAIKU_MODEL",
            "value": "deepseek-v4-flash"
        },
        {
            "name": "CLAUDE_CODE_EFFORT_LEVEL",
            "value": "max"
        },  
  ]
```

