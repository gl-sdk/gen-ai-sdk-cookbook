"""Runtime Config Demo.

Demonstrates runtime_config for tools, agents, and MCPs.
"""

from agents import research_agent
from dotenv import load_dotenv
from mcps import arxiv_mcp
from tools import ResearchFormatterTool
import os

load_dotenv(override=True)
_api_key = os.getenv("ARXIV_MCP_API_KEY")
_auth_token = os.getenv("ARXIV_MCP_AUTH_TOKEN")


def main() -> None:
    """Deploy and run the research agent with runtime_config."""
    print("=" * 60)
    print("Runtime Config Demo")
    print("=" * 60)

    research_agent.deploy()

    print("\n✓ Agent deployed successfully!")
    print(f"  ID: {research_agent.id}")
    print(f"  Name: {research_agent.name}")

    # Test run with runtime_config
    print("\n" + "=" * 60)
    print("Running with runtime_config overrides...")
    print("=" * 60)

    result = research_agent.run(
        "Hello! Can you help me find papers about transformers?",
        runtime_config={
            "agent_config": {"planning": True},
            "tool_configs": {
                ResearchFormatterTool: {
                    "style": "brief",
                    "max_results": 3,
                },
            },
            research_agent: {
                "mcp_configs": {
                    arxiv_mcp: {
                        "authentication": {
                            "type": "custom-header",
                            "headers": {
                                "x-api-key": _api_key,
                                "Authorization": f"Bearer {_auth_token}",
                            },
                        },
                    },
                },
            },
        },
    )

    print(f"\nResult:\n{result}")


if __name__ == "__main__":
    main()
