"""Multi-Agent Example.

This demonstrates the multi-agent coordinator pattern with:
- A coordinator agent that orchestrates sub-agents
- Sub-agents that share tools (tools are deployed only once)
- Caching to prevent duplicate deployments

Architecture:
    GreetingCoordinator (coordinator)
    ├── FormalGreeter (sub-agent) - formal greetings
    ├── CasualGreeter (sub-agent) - casual greetings
    └── Shared GreetingTool deployed only once

Pattern: Multi-agent with coordinator
Use when: Complex workflows requiring multiple specialized agents
"""

from agents import greeting_coordinator
from dotenv import load_dotenv

load_dotenv(override=True)


def main() -> None:
    """Deploy the multi-agent coordinator."""
    print("=" * 60)
    print("Multi-Agent Coordinator Example")
    print("=" * 60)

    deployed = greeting_coordinator.deploy()

    print("\n✓ Multi-agent system deployed successfully!")
    print(f"  Coordinator: {deployed.name} (ID: {deployed.id})")


if __name__ == "__main__":
    main()
