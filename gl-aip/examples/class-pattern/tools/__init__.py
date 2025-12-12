"""Hello World Subclass Agent - Tools module."""

from glaip_sdk.tools import Tool
from tools.greeting import GreetingTool

time_tool = Tool.from_native("time_tool")

__all__ = ["GreetingTool", "time_tool"]
