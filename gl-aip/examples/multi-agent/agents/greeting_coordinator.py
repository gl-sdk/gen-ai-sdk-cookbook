from agents.casual_greeter import casual_greeter
from agents.formal_greeter import formal_greeter
from glaip_sdk.agents import Agent

greeting_coordinator = Agent(
    name="greeting_coordinator",
    instruction="""You are a greeting coordinator managing two specialists:
1. formal_greeter - For professional, formal greetings
2. casual_greeter - For friendly, casual greetings and farewells

Delegate to the appropriate specialist based on context.""",
    description="Coordinates greeting specialists for personalized greetings",
    agents=[formal_greeter, casual_greeter],
)

__all__ = ["greeting_coordinator"]
