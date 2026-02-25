# Hello World - Runtime Config Demo

Demonstrates `runtime_config` for per-request overrides of agents, tools, and MCPs.

## Setup

```bash
cp .env.example .env
# Edit .env with your credentials
uv sync
```

## Usage

### Deploy Agent

```bash
uv run python main.py
```

### Run Demo

```bash
uv run python demo_runtime_config.py
```

## runtime_config Examples

### 1. agent_config

Override agent behavior (planning, temperature, etc.):

```python
agent.run("query", runtime_config={
    "agent_config": {"planning": True}
})
```

### 2. tool_configs

Override tool configuration using SDK class or ID:

```python
agent.run("query", runtime_config={
    "tool_configs": {
        ResearchFormatterTool: {"style": "academic", "max_results": 3}
    }
})
```

### 3. mcp_configs

Override MCP authentication at runtime:

```python
agent.run("query", runtime_config={
    "mcp_configs": {
        arxiv_mcp: {
            "authentication": {
                "type": "custom-header",
                "headers": {"x-api-key": "new-key"}
            }
        }
    }
})
```

## Key Patterns

- **SDK objects as keys**: Use `ResearchFormatterTool` or `arxiv_mcp` directly
- **Strings as keys**: Use tool/MCP names or UUIDs
- **Conditional MCPs**: `arxiv_mcp` only created if env vars are set
