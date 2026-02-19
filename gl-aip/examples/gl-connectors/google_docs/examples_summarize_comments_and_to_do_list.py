from dotenv import load_dotenv
import asyncio
import os

from glaip_sdk import Agent
from gllm_tools.mcp.client.langchain import LangchainMCPClient

load_dotenv()

DESIRED_TOOLS = {"google_docs_list_comments", "google_docs_summarize_comments", "google_docs_create_document", "google_docs_list_documents", "google_docs_get_document", "google_docs_update_document"}

client = LangchainMCPClient({
    "google_docs": {
        "url": "https://connector.gdplabs.id/google_docs/mcp",
        "headers": {"Authorization": f"Bearer {os.getenv('GL_CONNECTORS_USER_TOKEN')}"},
    }
})

FILE_NAME= "MCP Testing Report"

def extract_content(chunk) -> str | None:
    if isinstance(chunk, str):
        return chunk
    if isinstance(chunk, dict):
        return chunk.get("content")
    return getattr(chunk, "content", None)


async def main():
    all_tools = await client.get_tools("google_docs")
    print("Available tools:", [t.name for t in all_tools])
    tools = [t for t in all_tools if t.name in DESIRED_TOOLS]

    agent = Agent(
        name="google_docs_agent",
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
        f"Open the document named '{FILE_NAME}'." 
        "Create a new document. The inside of the document should have the summarized comments and structured list of 'Action Items' based on those comments so I know exactly what I need to revise."
        "After that, give me a brief tone analysis—are the reviewers happy or concerned on the document"
    )

    # Use async streaming for local execution
    async for chunk in deployed_agent.arun(prompt):
        if content := extract_content(chunk):
            print(content, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())