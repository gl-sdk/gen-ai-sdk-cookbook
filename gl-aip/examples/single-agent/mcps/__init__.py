"""Hello World Single Agent - MCPs module.

Exports MCP configurations for Model Context Protocol servers.
"""

from glaip_sdk.mcps import MCP

# DeepWiki MCP - provides access to public repository documentation
# Available tools:
#   - read_wiki_structure: Get list of documentation topics for a GitHub repo
#   - read_wiki_contents: View documentation about a GitHub repository
#   - ask_question: Ask questions about a GitHub repository
deepwiki_mcp = MCP(
    name="deepwiki",
    transport="sse",
    description="DeepWiki MCP for accessing public GitHub repository documentation",
    config={
        "url": "https://mcp.deepwiki.com/sse",
    },
)

__all__ = ["deepwiki_mcp"]
