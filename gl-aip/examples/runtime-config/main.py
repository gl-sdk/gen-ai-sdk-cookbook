"""Runtime Config Demo - runtime_config for agents, tools, and MCPs."""

import os
from agents import research_agent
from dotenv import load_dotenv
from mcps import arxiv_mcp
from tools import ResearchFormatterTool

load_dotenv(override=True)

if __name__ == "__main__":
    agent = research_agent.deploy()
    print(f"✓ Deployed: {agent.name} (ID: {agent.id})")

    result = research_agent.run(
        "Hello! Can you help me find papers about transformers?",
        runtime_config={
            "agent_config": {"planning": True},
            "tool_configs": {
                ResearchFormatterTool: {"style": "brief", "max_results": 3},
            },
            research_agent: {
                "mcp_configs": {
                    arxiv_mcp: {
                        "authentication": {
                            "type": "custom-header",
                            "headers": {
                                "x-api-key": os.getenv("ARXIV_MCP_API_KEY"),
                                "Authorization": f"Bearer {os.getenv('ARXIV_MCP_AUTH_TOKEN')}",
                            },
                        },
                    },
                },
            },
        },
    )
    print(f"\nResult:\n{result}")
