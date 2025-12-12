"""Hello Agent - Subclass pattern example.

This demonstrates the subclass-based Agent pattern where you create
a class that inherits from Agent and overrides properties.

Pattern: Subclass with property overrides
Use when: Reusable agents, complex configuration, shared base classes
"""

from glaip_sdk.agents import Agent
from tools import GreetingTool, time_tool


class HelloAgent(Agent):
    """A friendly greeting agent using the subclass pattern.

    This pattern is useful when you want:
    - Reusable agent definitions
    - Complex property logic
    - Loading instructions from files
    - Shared base class behavior

    Example:
        >>> deployed = HelloAgent().deploy()
        >>> print(f"Deployed: {deployed.name}")
    """

    @property
    def name(self) -> str:
        """Agent name on the AIP platform."""
        return "hello_agent_subclass"

    @property
    def description(self) -> str:
        """Agent description."""
        return "A friendly greeting agent (subclass pattern)"

    @property
    def instruction(self) -> str:
        """Agent instruction - can also load from file."""
        return """You are a friendly greeting assistant.

When users greet you or ask for a greeting:
1. Use the greeting tool to generate a personalized greeting
2. Be warm and welcoming
3. Keep responses concise
4. Use the time tool when users ask about the current time

You can greet users in different styles: formal, casual, or enthusiastic.
"""

    @property
    def tools(self) -> list:
        """Tools available to this agent."""
        return [GreetingTool, time_tool]

    @property
    def metadata(self) -> dict:
        """Agent metadata."""
        return {
            "version": "1.0.0",
            "pattern": "subclass",
        }


__all__ = ["HelloAgent"]
