from glaip_sdk.agents import Agent
from tools import greeting_tool, time_tool

formal_greeter = Agent(
    name="formal_greeter",
    instruction="You are a formal greeting specialist. Use the greeting tool with style='formal'.",
    description="Provides formal, professional greetings",
    tools=[greeting_tool, time_tool],
)

__all__ = ["formal_greeter"]
