from glaip_sdk.agents import Agent
from mcps import arxiv_mcp
from tools import ResearchFormatterTool

research_agent = Agent(
    name="research_agent",
    instruction="""You are a research assistant that helps find and format academic papers.
Use the arxiv MCP to search for papers and the research_formatter tool to format results.""",
    description="Research assistant with configurable formatting",
    tools=[ResearchFormatterTool],
    mcps=[arxiv_mcp] if arxiv_mcp else [],
)

__all__ = ["research_agent"]
