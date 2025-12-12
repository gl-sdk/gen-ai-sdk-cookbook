"""Hello Agent - config-based Agent() with MCP integration."""

from glaip_sdk.agents import Agent
from glaip_sdk.tools import Tool
from mcps import deepwiki_mcp
from tools import GreetingTool

time_tool = Tool.from_native("time_tool")

hello_agent = Agent(
    name="hello_agent",
    instruction="""You are a friendly greeting assistant with knowledge capabilities.

Use the greeting tool for personalized greetings (formal, casual, or enthusiastic).
Use the time tool when users ask about the current time.
Use DeepWiki tools to explore GitHub repository documentation.""",
    description="A friendly agent that greets users and can explore GitHub repos",
    tools=[GreetingTool, time_tool],
    mcps=[deepwiki_mcp],
)

__all__ = ["hello_agent"]
