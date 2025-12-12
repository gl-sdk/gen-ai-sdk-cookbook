"""Multi-Agent Example - coordinator pattern with sub-agents."""

from agents import greeting_coordinator
from dotenv import load_dotenv

load_dotenv(override=True)

if __name__ == "__main__":
    agent = greeting_coordinator.deploy()
    print(f"✓ Deployed: {agent.name} (ID: {agent.id})")
