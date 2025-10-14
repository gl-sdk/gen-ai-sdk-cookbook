from glaip_sdk import Client

client = Client()

tools = client.list_tools()
web_search_tool_id = next(
    (tool.id for tool in tools if "web_search" in tool.name.lower()),
    None,
)
if not web_search_tool_id:
    raise RuntimeError(
        "web_search tool not found. Enable it on the platform before running the demo."
    )

research_agent = client.create_agent(
    name="research_agent",
    instruction="""You are a research specialist. Use the web_search tool to gather up-to-date information and cite sources.""",
    model="gpt-4.1",
    tools=[web_search_tool_id],
)

information_compiler = client.create_agent(
    name="information_compiler",
    instruction="""You are an analyst who turns raw research notes into clear, well-structured summaries. Use Markdown and include URLs.""",
    model="gpt-4.1",
)

coordinator = client.create_agent(
    name="coordinator",
    instruction="""You oversee a hierarchical research system with two sub-agents:
    - "research_agent" gathers information
    - "information_compiler" formats the findings

    Workflow:
    1. Delegate the user's topic to research_agent
    2. Review the research output
    3. Forward the raw notes to information_compiler for formatting
    4. Deliver the final summary back to the user""",
    model="gpt-4.1",
    agents=[research_agent.id, information_compiler.id],
)

topic = "Latest developments in artificial intelligence for healthcare in 2025"
coordinator.run(f"Please research and summarize: {topic}")

coordinator.delete()
information_compiler.delete()
research_agent.delete()
