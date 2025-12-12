"""Single Agent - MCPs module."""

from glaip_sdk.mcps import MCP

deepwiki_mcp = MCP(
    name="deepwiki",
    transport="sse",
    description="DeepWiki MCP for accessing public GitHub repository documentation",
    config={"url": "https://mcp.deepwiki.com/sse"},
)

__all__ = ["deepwiki_mcp"]
