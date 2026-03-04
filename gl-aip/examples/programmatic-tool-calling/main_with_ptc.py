"""Scenario demo with Programmatic Tool Calling (PTC)."""

from dotenv import load_dotenv

from glaip_sdk.agents import Agent
from glaip_sdk.ptc import PTC
from tools import GetOrdersTool, GetUserTool

load_dotenv(override=True)

query = "What did Alice order recently, and what's her email so I can follow up?"

agent = Agent(
    name="customer_followup_with_ptc",
    model="openai/gpt-5.2",
    instruction=(
        "You are a customer support assistant. "
        "Always use execute_ptc_code for data retrieval workflows. "
        "Inside execute_ptc_code, call get_user(name) first, then call get_orders(user_id) using the returned id. "
        "If any tool returns status='not_found', explain it clearly and do not guess."
    ),
    tools=[GetUserTool(), GetOrdersTool()],
    ptc=PTC(enabled=True, sandbox_timeout=180.0),
)

agent.run(query, local=True, verbose=True)
