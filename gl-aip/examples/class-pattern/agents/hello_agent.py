from glaip_sdk.agents import Agent
from tools import GreetingTool, time_tool


class HelloAgent(Agent):
    """Subclass-based Agent pattern example."""

    @property
    def name(self) -> str:
        return "hello_agent_subclass"

    @property
    def description(self) -> str:
        return "A friendly greeting agent (subclass pattern)"

    @property
    def instruction(self) -> str:
        return """You are a friendly greeting assistant.
Use the greeting tool for personalized greetings (formal, casual, or enthusiastic).
Use the time tool when users ask about the current time."""

    @property
    def tools(self) -> list:
        return [GreetingTool, time_tool]

    @property
    def metadata(self) -> dict:
        return {"version": "1.0.0", "pattern": "subclass"}


__all__ = ["HelloAgent"]
