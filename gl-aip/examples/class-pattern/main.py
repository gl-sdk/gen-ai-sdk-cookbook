"""Class Pattern Agent Example.

This demonstrates the subclass-based Agent pattern where you
create a class that inherits from Agent and overrides properties.

Pattern: Subclass with property overrides
Use when: Reusable agents, complex configuration, shared base classes
"""

from agents import HelloAgent
from dotenv import load_dotenv

load_dotenv(override=True)


def main() -> None:
    """Deploy the agent using subclass pattern."""
    print("=" * 60)
    print("Class Pattern Agent Example")
    print("=" * 60)

    # Instantiate and deploy - the class handles all configuration
    deployed = HelloAgent().deploy()

    print("\n✓ Agent deployed successfully!")
    print(f"  ID: {deployed.id}")
    print(f"  Name: {deployed.name}")


if __name__ == "__main__":
    main()
