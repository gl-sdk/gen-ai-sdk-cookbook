from glaip_sdk import Client

client = Client()

tools = client.list_tools()
bosa_sql_query_tool_id = next(
    (tool.id for tool in tools if "bosa_sql_query" in tool.name.lower()),
    None,
)
if not bosa_sql_query_tool_id:
    raise RuntimeError(
        "bosa_sql_query tool not found. Enable it on the platform before running the demo."
    )

agent = client.create_agent(
    name="bosa-sql-query-agent",
    instruction="You are a friendly AI assistant. Use the bosa_sql_query tool to query the database.",
    model="gpt-4.1",
    tools=[bosa_sql_query_tool_id],
)

agent.run(
    "How many tables are in the database?",
    runtime_config={
        "agent_config": {
            "lm_hyperparameters": {"temperature": 0.2},
        },
        "tool_configs": {
            bosa_sql_query_tool_id: {
                "database_url": "postgresql://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs",
            },
        },
    },
)
agent.delete()
