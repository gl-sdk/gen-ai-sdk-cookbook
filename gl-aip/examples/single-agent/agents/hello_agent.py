"""Hello Agent - Simple single agent example.

This demonstrates the config-based Agent() pattern with MCP integration.
"""

from glaip_sdk.agents import Agent
from glaip_sdk.tools import Tool
from mcps import deepwiki_mcp
from tools import GreetingTool

# Native platform tool
time_tool = Tool.from_native("time_tool")

INSTRUCTION = """You are a friendly greeting assistant with knowledge capabilities.

When users greet you or ask for a greeting:
1. Use the greeting tool to generate a personalized greeting
2. Be warm and welcoming
3. Keep responses concise
4. Use the time tool when users ask about the current time

You also have access to DeepWiki for exploring GitHub repository documentation.
When users ask about a GitHub repository:
1. Use read_wiki_structure to see available documentation topics
2. Use read_wiki_contents to read specific documentation
3. Use ask_question to answer questions about the repository

You can greet users in different styles: formal, casual, or enthusiastic.
"""

hello_agent = Agent(
    name="hello_agent",
    instruction=INSTRUCTION,
    description="A friendly agent that greets users and can explore GitHub repos",
    tools=[GreetingTool, time_tool],
    mcps=[deepwiki_mcp],
)

__all__ = ["hello_agent"]
