# 🍧 GL AIP (GDP Labs AI Agent Package) Cookbook

Welcome to the **GL AIP Cookbook** - a comprehensive collection of sample code and examples for working with the GL AIP SDK.

## ⚙️ Prerequisites

### 1. Base Requirements (all examples)

- Python 3.11 or 3.12
- [uv](https://docs.astral.sh/uv/) package manager

### 2. Server-backed examples (requires deployment)

These examples call `agent.deploy()` and require AIP credentials:

- `examples/hello-world`
- `examples/multi-agent`
- `examples/runtime-config`
- `examples/modular-tool-integration`
- `examples/agent-export-import`

Set:

```bash
export AIP_API_KEY="your_api_key_here"
export AIP_API_URL="your_aip_api_url"
```

### 3. Local-run examples (no deployment)

These examples run locally and do **not** require `AIP_API_KEY` / `AIP_API_URL`:

- `examples/hello-world-local`
- `examples/multi-agent-system-patterns`

Set at least:

```bash
export OPENAI_API_KEY="your_openai_key_here"
```

Some local examples need additional optional keys (for MCP/native tools). See each example's README for details.

## 🚀 Getting Started

Explore the subdirectories in the [examples](./examples/) folder for specific setup instructions and code examples.
