[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/melbourneandrew-docs2prompt-mcp-badge.png)](https://mseep.ai/app/melbourneandrew-docs2prompt-mcp)

# MCP Server for docs2prompt

[![](https://badge.mcpx.dev?type=server 'MCP Server')](https://modelcontextprotocol.io/introduction)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/rezabrizi/docs2prompt/blob/main/LICENSE)

[docs2prompt](https://github.com/rezabrizi/docs2prompt) is a python library and line tool developed by [Reza Tabrizi](https://github.com/rezabrizi) that turns documentation in github repositories or hosted on dedicated websites into LLM-friendly prompts.

This repository contains an MCP server that wraps docs2prompt for use by any MCP client (Cursor, Claude, Windsurf, etc).

## Run Server (Development)
1. [Install UV](https://docs.astral.sh/uv/getting-started/installation/)
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Clone the repository:
```
git clone https://github.com/Melbourneandrew/docs2prompt-mcp
```

3. Put this in your MCP client config (Add your path and [github access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)):
```
{
    "mcpServers": {
        "docs2prompt": {
            "command": "uv",
            "args": [
                "--directory",
                "/YOUR/LOCAL/PATH/docs2prompt-mcp/src",
                "run",
                "main.py"
            ],
            "env": {
                "GITHUB_TOKEN": ""
            }
        }
    }
}
```

If you need, here are guides to set up MCP for common clients:
* [Cursor](https://docs.cursor.com/context/model-context-protocol)
* [Claude Desktop](https://modelcontextprotocol.io/quickstart/server#test-with-commands)