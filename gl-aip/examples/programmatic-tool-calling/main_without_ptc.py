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
        "You are a finance audit assistant. "
        "You must audit all Engineering team members end-to-end. "
        "Important: call exactly one tool per assistant turn. "
        "Do not batch multiple tool calls in one turn. "
        "Use get_team_members(department='Engineering'), then for each member call get_expenses(user_id, quarter='Q3'), "
        "then call get_budget_by_level(level). "
        "Team members are at team_result['data']['members']. "
        "Compute totals and return only members who exceeded budget sorted by overage descending. "
        "Do not skip members and do not estimate."
    ),
    tools=[GetTeamMembersTool(), GetExpensesTool(), GetBudgetByLevelTool()],
)

agent.run(query, local=True, verbose=True)
