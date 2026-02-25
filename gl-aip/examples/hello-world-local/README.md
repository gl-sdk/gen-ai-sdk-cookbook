# Hello World - Local Agent Execution

This example demonstrates how to run a GLAIP SDK agent **locally** without deploying to the AIP server.

## Features

- Local Execution: runs directly on your machine using local mode.
- No Deploy Required: define and run - no server needed.
- Quick Prototyping: good for development and testing.
- Tool Support: LangChain BaseTool classes can be used locally.

## Prerequisites

### Base Installation

Install all dependencies using `uv sync`:

```bash
cd examples/hello-world-local
uv sync
```

This installs local dependencies and sets up your virtual environment.

### Optional installation

```bash
# Using pip
pip install "glaip-sdk[local]"

# Using uv directly
uv sync
```

### Required Environment Variables

**Minimum Required (for all examples):**

- `OPENAI_API_KEY`: required for the LLM provider (or configure another provider in aip-agents)

**Example-Specific Environment Variables:**

| Example | Required Environment Variables | Notes |
| --- | --- | --- |
| `main_with_memory.py` | `MEM0_API_KEY` or `GLLM_MEMORY_API_KEY` | Either one works |
| `main_with_native_tool.py --serper` | `SERPER_API_KEY` | Google Serper web search API key |
| `main_with_native_tool.py --e2b` | `E2B_API_KEY` | E2B code sandbox API key |
| `main_with_native_tool.py --browser` | None | Browser Use tool doesn't require an API key |
| `main_with_gl_connectors_tool.py` | `GL_CONNECTORS_BASE_URL`<br>`GL_CONNECTORS_API_KEY`<br>`GL_CONNECTORS_USERNAME`<br>`GL_CONNECTORS_PASSWORD`<br>`GL_CONNECTORS_IDENTIFIER` (optional) | Backward compatible with `BOSA_*` values |
| `main_with_mcp.py`<br>`main_with_agent_definition_configs.py`<br>`main_with_runtime_config.py` | `ARXIV_MCP_API_KEY`<br>`ARXIV_MCP_AUTH_TOKEN` | Optional, for Arxiv MCP server |

**Option 1: Export in shell**

```bash
export OPENAI_API_KEY="your-key-here"
export MEM0_API_KEY="your-mem0-key"
export SERPER_API_KEY="your-serper-key"
export E2B_API_KEY="your-e2b-key"
export GL_CONNECTORS_BASE_URL="https://your-gl-connector-url"
export GL_CONNECTORS_API_KEY="your-api-key"
export GL_CONNECTORS_USERNAME="your-username"
export GL_CONNECTORS_PASSWORD="your-password"
```

**Option 2: Create a `.env` file**

```bash
cp .env.example .env
# Edit .env with your API keys
```

## Usage

Run examples with `uv run`:

```bash
uv run python <example_file>.py
```

## Available Examples

| Example File | Command | Description |
| --- | --- | --- |
| `main.py` | `uv run python main.py` | basic local agent execution |
| `main_with_chat_history.py` | `uv run python main_with_chat_history.py` | add chat history |
| `main_with_local_files.py` | `uv run python main_with_local_files.py` | local file access |
| `main_with_docproc_pdf.py` | `uv run python main_with_docproc_pdf.py` | PDF document processing |
| `main_with_agent_definition_configs.py` | `uv run python main_with_agent_definition_configs.py` | agent runtime configuration |
| `main_with_runtime_config.py` | `uv run python main_with_runtime_config.py` | runtime configuration |
| `main_with_pii_toggle.py` | `uv run python main_with_pii_toggle.py` | PII redaction toggle |
| `main_with_hitl.py` | `uv run python main_with_hitl.py` | human-in-the-loop approval |
| `main_with_memory.py` | `uv run python main_with_memory.py` | mem0 memory backend |
| `main_with_subagents.py` | `uv run python main_with_subagents.py` | subagents |
| `main_with_tool_output_sharing.py` | `uv run python main_with_tool_output_sharing.py` | tool output sharing |
| `main_with_a2a_token_streaming.py` | `uv run python main_with_a2a_token_streaming.py` | A2A token streaming |
| `main_with_mcp.py` | `uv run python main_with_mcp.py` | MCP integration |
| `main_with_gl_connectors_tool.py` | `uv run python main_with_gl_connectors_tool.py` | GL Connectors integration |
| `main_with_native_tool.py --all`<br>`uv run python main_with_native_tool.py --e2b`<br>`uv run python main_with_native_tool.py --serper`<br>`uv run python main_with_native_tool.py --browser` | `uv run python main_with_native_tool.py --query "..."` | native tools examples |
