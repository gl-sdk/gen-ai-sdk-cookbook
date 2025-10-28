"""Direct execution example for BOSA MCP with pre-configured credentials.

This script demonstrates BOSA MCP usage when all credentials are already
configured in the environment. It assumes you have:
- BOSA_CLIENT_KEY set in your environment
- BOSA_IDENTIFIER and BOSA_USER_SECRET for authentication
- Existing GitHub integration

For interactive setup, use src/main.py instead.

Authors:
    Samuel Lusandi (samuel.lusandi@gdplabs.id)
"""

import asyncio
import os
from typing import cast

from bosa_connectors import BosaConnector
from dotenv import load_dotenv

from mcp import ClientSession
from gllm_tools.mcp.client.session import create_session

load_dotenv()

bosa_api_url = os.getenv("BOSA_API_URL") or "https://api.bosa.id"
bosa_client_key = os.getenv("BOSA_CLIENT_KEY")

bosa_connector = BosaConnector(
    api_base_url=bosa_api_url,
    api_key=bosa_client_key,
)

user_identifier = os.getenv("BOSA_IDENTIFIER")
user_secret = os.getenv("BOSA_USER_SECRET")

if not user_identifier or not user_secret:
    print("❌ User identifier or user secret is not set. Please set them in the .env file.")
    print("💡 Tip: Use 'uv run src/main.py' for interactive setup instead.")
    exit(1)

print("🔐 Authenticating with BOSA...")
try:
    bosa_token = bosa_connector.authenticate_bosa_user(user_identifier, user_secret).token
    print("✅ Authentication successful!")
except Exception as e:
    print(f"❌ Authentication failed: {e}")
    print("Please check your BOSA_IDENTIFIER and BOSA_USER_SECRET.")
    exit(1)

print("🔍 Getting user information...")
try:
    user_info = bosa_connector.get_user_info(bosa_token)
    print(f"✅ User ID: {user_info.id}")
    print(f"✅ Identifier: {user_info.identifier}")
except Exception as e:
    print(f"❌ Error getting user info: {e}")
    print("Please check your credentials and try again.")
    exit(1)

print("🔍 Checking GitHub integration...")
try:
    if not bosa_connector.user_has_integration("github", bosa_token):
        print("❌ GitHub integration not found!")
        print("Please set up GitHub integration first:")
        print("1. Run 'uv run src/main.py' for interactive setup, or")
        print("2. Visit your BOSA console to set up GitHub integration manually")
        create_github_integration = bosa_connector.initiate_connector_auth("github", bosa_token, "http://localhost:8000")
        print(f"3. Or open this URL: {create_github_integration}")
        exit(1)
    else:
        print("✅ GitHub integration is active!")
except Exception as e:
    print(f"❌ Error checking GitHub integration: {e}")
    exit(1)

bosa_configuration = {
    "transport": "streamable_http",
    "url": f"{bosa_api_url}/github/mcp",
    "headers": {
        "Authorization": f"Bearer {bosa_token}",
        "X-Api-Key": bosa_client_key,
    }
}

async def main() -> None:
    """Main function to execute BOSA MCP GitHub issue retrieval.
    
    This function demonstrates a complete MCP workflow:
    1. Establishes MCP session with BOSA GitHub connector
    2. Prompts user for GitHub repository details
    3. Executes the github_get_issue_handler tool
    4. Displays the results
    
    Raises:
        Exception: If MCP session cannot be established or tool execution fails.
        ValueError: If invalid issue number is provided.
    """
    print("🚀 Connecting to BOSA GitHub MCP...")
    try:
        async with create_session(bosa_configuration) as session:
            await session.initialize()
            print("✅ MCP session initialized successfully!")
            
            print("\n📝 Please provide GitHub repository details:")
            try:
                owner = input("  Repository owner (e.g., 'octocat'): ").strip()
                repo = input("  Repository name (e.g., 'Hello-World'): ").strip()
                issue_number_str = input("  Issue number (e.g., '1'): ").strip()
                
                if not owner or not repo or not issue_number_str:
                    print("❌ All fields are required.")
                    return
                
                issue_number = int(issue_number_str)
                if issue_number <= 0:
                    print("❌ Issue number must be a positive integer.")
                    return
                    
            except ValueError:
                print("❌ Invalid issue number. Please enter a valid integer.")
                return
            except KeyboardInterrupt:
                print("\n❌ Operation cancelled by user.")
                return

            tool_name = "github_get_issue_handler"
            params = {
                "owner": owner,
                "repo": repo,
                "issue_number": issue_number,
            }
            request = {"request": params}

            print(f"\n🚀 Executing tool '{tool_name}' with params: {params}")
            call_tool_result = await cast(ClientSession, session).call_tool(tool_name, request)

            print("\n✅ Tool execution completed successfully!")
            print("📋 Result:")
            print(call_tool_result)
            
    except Exception as e:
        print(f"❌ Error executing MCP tool: {e}")
        print("Please check your network connection and configuration.")

if __name__ == "__main__":
    asyncio.run(main())
