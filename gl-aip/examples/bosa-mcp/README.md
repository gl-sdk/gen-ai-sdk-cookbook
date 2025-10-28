# BOSA MCP Example Project

This project demonstrates how to integrate BOSA (Business Operations & Service Automation) connectors with GLLM (Generative Language Learning Model) tools using the Model Control Protocol (MCP). The example shows how to authenticate with BOSA services, set up GitHub integration, and execute MCP tools.

## Features

- 🔐 Interactive BOSA authentication setup
- 🔗 GitHub integration management
- 🛠️ MCP tool execution examples
- 📝 Comprehensive error handling and user guidance
- 🌐 Cross-platform browser launching utilities

## Prerequisites

- **Python 3.12 or higher**
- **[uv](https://github.com/astral-sh/uv) package manager** - Fast Python package installer and resolver
- **BOSA Account** - Access to BOSA API services
- **GitHub Account** - For GitHub integration features

## Quick Start

### 1. Project Setup

Clone or navigate to the project directory:
```bash
cd bosa-mcp
```

Install dependencies using uv:
```bash
uv sync
```

### 2. Environment Configuration

Create your environment configuration file:
```bash
cp .env.example .env
```

Edit the `.env` file with your BOSA credentials:
```env
# Required: BOSA API Configuration
BOSA_API_URL=https://api.bosa.id
BOSA_CLIENT_KEY=your-client-key-here

# For manual authentication
BOSA_IDENTIFIER=your-user-identifier
BOSA_USER_SECRET=your-user-secret
```

### 3. Running the Application

#### Interactive Setup (Recommended)
For first-time users or when setting up new credentials:
```bash
uv run src/main.py
```

This interactive script will:
- Guide you through obtaining your BOSA Client Key
- Help you set up your BOSA User Token
- Automatically configure GitHub integration
- Test the MCP connection with a sample GitHub issue query

#### Direct Execution
If you already have all credentials configured:
```bash
uv run example_all_setup.py
```

This script assumes you have:
- `BOSA_CLIENT_KEY` set in your environment
- `BOSA_IDENTIFIER` and `BOSA_USER_SECRET` for authentication
- Existing GitHub integration

## Project Structure

```
bosa-mcp/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # Interactive setup and MCP demo
│   └── utilities.py         # Helper functions for env and browser
├── example_all_setup.py     # Direct execution example
├── pyproject.toml           # Project configuration and dependencies
├── README.md                # This documentation
├── .env.example             # Environment variables template
└── uv.lock                  # Locked dependency versions
```

## Configuration Details

### Environment Variables

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `BOSA_API_URL` | No | BOSA API base URL | `https://api.bosa.id` |
| `BOSA_CLIENT_KEY` | Yes | Your BOSA client API key | `sk-client...` |
| `BOSA_IDENTIFIER` | Conditional | User identifier | `user@example.com` |
| `BOSA_USER_SECRET` | Conditional | User secret | `sk-user-...` |

## Usage Examples

### Basic GitHub Issue Retrieval with GLLM Tools

```python
import asyncio
from gllm_tools.mcp.client.session import create_session

# Configure BOSA MCP connection
bosa_configuration = {
    "transport": "streamable_http",
    "url": "https://api.bosa.id/github/mcp",
    "headers": {
        "Authorization": f"Bearer {bosa_token}",
        "X-Api-Key": client_key,
    }
}

async def get_github_issue():
    async with create_session(bosa_configuration) as session:
        await session.initialize()
        
        result = await session.call_tool("github_get_issue_handler", {
            "request": {
                "owner": "octocat",
                "repo": "Hello-World",
                "issue_number": 1
            }
        })
        
        print(result)

asyncio.run(get_github_issue())
```

## Development

### Adding Dependencies
```bash
uv add package-name
```

### Updating Dependencies
```bash
uv sync --upgrade
```

### Running Tests
```bash
uv run pytest  # When tests are added
```

## Troubleshooting

### Common Issues

**Authentication Errors**
- Verify your `BOSA_CLIENT_KEY` is correct
- Ensure your user token hasn't expired
- Check that your account has the necessary permissions

**GitHub Integration Issues**
- Complete the GitHub OAuth flow in your browser
- Verify the integration appears in your BOSA console
- Check that you have access to the target repository

**MCP Connection Problems**
- Confirm the BOSA API URL is accessible
- Verify your network connection
- Check that all required headers are included

### Getting Help

1. Check the BOSA Console at your configured API URL
2. Verify your account status and integrations
3. Review the error messages for specific guidance
4. Ensure all environment variables are properly set

## License

This project is part of the BOSA MCP cookbook examples.

