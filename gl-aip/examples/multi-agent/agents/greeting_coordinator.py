"""Greeting Coordinator - orchestrates greeting sub-agents."""

from agents.casual_greeter import casual_greeter
from agents.formal_greeter import formal_greeter
from glaip_sdk.agents import Agent

INSTRUCTION = """You are a greeting coordinator.

You manage two specialist agents:
1. formal_greeter - For professional, formal greetings
2. casual_greeter - For friendly, casual greetings and farewells

When a user wants to greet someone:
1. Determine the appropriate style based on context
2. Delegate to the appropriate specialist agent
3. For business/professional contexts, use formal_greeter
4. For friendly/casual contexts, use casual_greeter
"""

greeting_coordinator = Agent(
    name="greeting_coordinator",
    instruction=INSTRUCTION,
    description="Coordinates greeting specialists for personalized greetings",
    agents=[formal_greeter, casual_greeter],
)

__all__ = ["greeting_coordinator"]
