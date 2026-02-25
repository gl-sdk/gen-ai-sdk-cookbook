# Hello World - Single Agent

A minimal example demonstrating the simplest way to deploy an agent using direct `Agent()` instantiation.

**Pattern:** Config-based `Agent()` instantiation
**Use when:** Simple agents, quick prototypes, one-off deployments

## Quick Start

1. **Setup environment**

   ```bash
   cp .env.example .env
   # Edit .env with your AIP_API_URL and AIP_API_KEY
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Deploy the agent**

   ```bash
   uv run main.py
   ```

## Project Structure

```
hello-world-single-agent/
├── agents/
│   └── hello_agent.py    # Agent definition
├── tools/
│   └── greeting.py       # Custom LangChain tool
├── main.py               # Entry point
├── pyproject.toml
└── .env.example
```
