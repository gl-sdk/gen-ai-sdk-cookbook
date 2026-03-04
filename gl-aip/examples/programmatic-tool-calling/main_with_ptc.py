"""Scenario demo with Programmatic Tool Calling (PTC)."""

from dotenv import load_dotenv

from glaip_sdk.agents import Agent
from glaip_sdk.ptc import PTC
from tools import GetBudgetByLevelTool, GetExpensesTool, GetTeamMembersTool

load_dotenv(override=True)

query = "Which Engineering team members exceeded their Q3 travel budget?"

agent = Agent(
    name="budget_audit_with_ptc",
    model="openai/gpt-5.2",
    instruction=(
        "You are a finance audit assistant. "
        "Always use execute_ptc_code for this workflow. "
        "Call execute_ptc_code exactly once and do all looping/aggregation inside that single code execution. "
        "Inside execute_ptc_code: "
        "(1) call get_team_members(department='Engineering'), "
        "(2) read members from team_result['data']['members'], then loop and call get_expenses(user_id=member['id'], quarter='Q3'), "
        "(3) call get_budget_by_level(level=member['level']), "
        "(4) sum expense item amounts in code and compute overage. "
        "Use expense response at result['data']['items'] and budget response at result['data']['quarterly_budget']. "
        "Return only exceeded members sorted by overage descending. "
        "Write defensive code that validates status=='ok' before accessing fields."
    ),
    tools=[GetTeamMembersTool(), GetExpensesTool(), GetBudgetByLevelTool()],
    ptc=PTC(enabled=True, sandbox_timeout=180.0),
)

agent.run(query, local=True, verbose=True)
