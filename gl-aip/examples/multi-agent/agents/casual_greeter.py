from glaip_sdk.agents import Agent
from tools import farewell_tool, greeting_tool, time_tool

casual_greeter = Agent(
    name="casual_greeter",
    instruction="You are a casual greeting specialist. Use greeting tool with style='casual' or 'enthusiastic'. Use farewell tool for goodbyes.",
    description="Provides casual, friendly greetings and farewells",
    tools=[greeting_tool, farewell_tool, time_tool],
)

__all__ = ["casual_greeter"]
