"""Scenario demo without Programmatic Tool Calling (PTC)."""

from dotenv import load_dotenv

from glaip_sdk.agents import Agent
from tools import GetOrdersTool, GetUserTool

load_dotenv(override=True)

query = "What did Alice order recently, and what's her email so I can follow up?"

agent = Agent(
    name="customer_followup_without_ptc",
    model="openai/gpt-5.2",
    instruction=(
        "You are a customer support assistant. "
        "Use get_user first to find the customer, then use get_orders with the returned user_id. "
        "If any tool returns status='not_found', explain that clearly and do not guess."
    ),
    tools=[GetUserTool(), GetOrdersTool()],
)

agent.run(query, local=True, verbose=True)
