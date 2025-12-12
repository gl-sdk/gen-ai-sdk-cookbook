# Class Pattern

An example demonstrating the subclass-based Agent pattern where you create a class that inherits from `Agent` and overrides properties.

**Pattern:** Subclass with property overrides
**Use when:** Reusable agents, complex configuration, shared base classes

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
class-pattern/
├── agents/
│   └── hello_agent.py    # Agent class definition
├── tools/
│   └── greeting.py       # Custom LangChain tool
├── main.py               # Entry point
├── pyproject.toml
└── .env.example
```
