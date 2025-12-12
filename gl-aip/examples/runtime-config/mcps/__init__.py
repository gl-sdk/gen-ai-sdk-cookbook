"""Runtime Config - MCPs module."""

import os
from glaip_sdk.mcps import MCP
from dotenv import load_dotenv

load_dotenv(override=True)

_api_key = os.getenv("ARXIV_MCP_API_KEY")
_auth_token = os.getenv("ARXIV_MCP_AUTH_TOKEN")

arxiv_mcp: MCP | None = None
if _api_key and _auth_token:
    arxiv_mcp = MCP(
        name="arxiv-mcp-chen",
        transport="http",
        description="Arxiv MCP for searching academic papers",
        config={"url": "https://api.bosa.id/arxiv/mcp"},
        authentication={
            "type": "custom-header",
            "headers": {
                "x-api-key": _api_key,
                "Authorization": f"Bearer {_auth_token}",
            },
        },
    )

__all__ = ["arxiv_mcp"]
