"""Multi-Agent - Tools module."""

from glaip_sdk.tools import Tool
from tools.farewell import FarewellTool
from tools.greeting import GreetingTool

time_tool = Tool.from_native("time_tool")
greeting_tool = GreetingTool
farewell_tool = FarewellTool

__all__ = [
    "FarewellTool",
    "GreetingTool",
    "farewell_tool",
    "greeting_tool",
    "time_tool",
]
