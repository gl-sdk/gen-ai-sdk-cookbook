from gllm_plugin.tools import tool_plugin
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field


class GreetingInput(BaseModel):
    name: str = Field(..., description="Name of the person to greet")
    style: str = Field(
        default="casual", description="Style: formal, casual, or enthusiastic"
    )


@tool_plugin(version="1.0.0")
class GreetingTool(BaseTool):
    name: str = "greeting"
    description: str = "Generate a personalized greeting for someone"
    args_schema: type[BaseModel] = GreetingInput

    def _run(self, name: str, style: str = "casual") -> str:
        greetings = {
            "formal": f"Good day, {name}. It is a pleasure to meet you.",
            "casual": f"Hey {name}! How's it going?",
            "enthusiastic": f"WOW! {name}! SO GREAT to meet you! 🎉",
        }
        return greetings.get(style, greetings["casual"])
