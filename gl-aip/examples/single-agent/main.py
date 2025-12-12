"""Single Agent Example - config-based Agent() pattern."""

from agents import hello_agent
from dotenv import load_dotenv

load_dotenv(override=True)

if __name__ == "__main__":
    agent = hello_agent.deploy()
    print(f"✓ Deployed: {agent.name} (ID: {agent.id})")
