"""Single Agent Example.

This demonstrates the simplest way to deploy an agent using
the config-based Agent() pattern.

Pattern: Direct instantiation with Agent()
Use when: Simple agents, quick prototypes, one-off agents
"""

from agents import hello_agent

from dotenv import load_dotenv

load_dotenv(override=True)


def main() -> None:
    """Deploy the single agent."""
    print("=" * 60)
    print("Single Agent Example")
    print("=" * 60)

    deployed = hello_agent.deploy()

    print("\n✓ Agent deployed successfully!")
    print(f"  ID: {deployed.id}")
    print(f"  Name: {deployed.name}")


if __name__ == "__main__":
    main()
