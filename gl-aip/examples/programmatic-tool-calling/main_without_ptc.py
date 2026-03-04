"""Scenario demo without Programmatic Tool Calling (PTC)."""

from dotenv import load_dotenv

from glaip_sdk.agents import Agent
from tools import GetBudgetByLevelTool, GetExpensesTool, GetTeamMembersTool

load_dotenv(override=True)

query = "Which Engineering team members exceeded their Q3 travel budget?"

agent = Agent(
    name="budget_audit_without_ptc",
    model="openai/gpt-5.2",
    instruction=(
        "You are a finance audit assistant with tool access. "
        "Use tools when needed, validate tool responses before reading nested fields, "
        "handle not_found/error statuses safely, and avoid guessing. "
        "Perform any required calculations from tool data and return concise final results."
    ),
    tools=[GetTeamMembersTool(), GetExpensesTool(), GetBudgetByLevelTool()],
)

agent.run(query, local=True, verbose=True)
