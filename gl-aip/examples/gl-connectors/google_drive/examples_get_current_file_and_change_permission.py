from dotenv import load_dotenv
import asyncio
import os

from glaip_sdk import Agent
from gllm_tools.mcp.client.langchain import LangchainMCPClient

load_dotenv()

DESIRED_TOOLS = {"google_drive_recent_files", "google_drive_list_permissions", "google_drive_update_permission"}

client = LangchainMCPClient({
    "google_drive": {
        "url": "https://connector.gdplabs.id/google_drive/mcp",
        "headers": {"Authorization": f"Bearer {os.getenv('GL_CONNECTORS_USER_TOKEN')}"},
    }
})

YOUR_EMAIL = "example@gmail.com"

def extract_content(chunk) -> str | None:
    if isinstance(chunk, str):
        return chunk
    if isinstance(chunk, dict):
        return chunk.get("content")
    return getattr(chunk, "content", None)

async def main():
    all_tools = await client.get_tools("google_drive")
    tools = [t for t in all_tools if t.name in DESIRED_TOOLS]

    agent = Agent(
        name="google_drive_agent",
        instruction="You are a helpful assistant.",
        tools=tools,
        model="gpt-5", # Use gpt-5 because it has better reasoning capabilities to understand the instruction and use the tool correctly
    )
    
    # Deploy the agent (with [local] extras, it will run locally using OPENAI_API_KEY)
    try:
        deployed_agent = agent.deploy()
        print(f"✓ Agent ready: {deployed_agent.name}")
    except Exception as e:
        print(f"Note: {e}")
        # Continue anyway for local execution
        deployed_agent = agent

    prompt = (
        "Find the 5 most recent files I've worked on and owned by me."
        "For each of these files, list who has access to them using the permissions tool."
        "If any of them are 'Public' or have 'Anyone with the link' access, "
        f"change their permission to 'Private' but make sure my email {YOUR_EMAIL} remains as the owner with full access."
    )

    # Use async streaming for local execution
    async for chunk in deployed_agent.arun(prompt):
        if content := extract_content(chunk):
            print(content, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())