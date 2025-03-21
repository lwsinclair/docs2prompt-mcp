from mcp.server.fastmcp import FastMCP
from docs2prompt import get_github_documentation, get_url_documentation
import os

mcp = FastMCP("docs2prompt")

@mcp.tool()
async def get_docs2prompt_docs(github_repo: str):
    """
    Use this tool to get the documentation from a GitHub repository.

    Args:
        github_repo: The GitHub repository to get the documentation for.
    """

    if "github.com/" in github_repo:
        parts = github_repo.split("github.com/")[1].split("/")
        github_repo = f"{parts[0]}/{parts[1]}"
    
    github_token = os.getenv("GITHUB_TOKEN", None)     
    result = get_github_documentation(github_repo, github_token)
    # Limit for longest possible response needs to be explored
    # Asking for https://github.com/browser-use/browser-use seems to crash the server

    return result[:10000] if result else result

@mcp.tool()
async def get_url_docs(url: str):
    """
    Use this tool to get the documentation at a URL.

    Args:
        url: The URL to get the documentation for.
    """
    return get_url_documentation(url)

if __name__ == "__main__":
    mcp.run(transport='stdio')