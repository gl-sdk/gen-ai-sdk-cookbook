"""Class Pattern Example - subclass-based Agent pattern."""

from agents import HelloAgent
from dotenv import load_dotenv

load_dotenv(override=True)

if __name__ == "__main__":
    agent = HelloAgent().deploy()
    print(f"✓ Deployed: {agent.name} (ID: {agent.id})")
