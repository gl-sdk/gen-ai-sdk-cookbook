"""Research Agent - Demonstrates runtime_config with tools and MCP."""

from glaip_sdk.agents import Agent
from mcps import arxiv_mcp
from tools import ResearchFormatterTool

INSTRUCTION = """You are a research assistant that helps find and format academic papers.

When users ask about research topics:
1. Use the arxiv MCP to search for papers (if available)
2. Use the research_formatter tool to format results

You can format results in different styles: brief, detailed, or academic.
"""

# Build tools and MCPs lists
_tools: list = [ResearchFormatterTool]
_mcps: list = [arxiv_mcp] if arxiv_mcp else []

research_agent = Agent(
    name="research_agent",
    instruction=INSTRUCTION,
    description="Research assistant with configurable formatting",
    tools=_tools,
    mcps=_mcps,
)

__all__ = ["research_agent"]
