# Programmatic Tool Calling

A minimal example demonstrating programmatic tool calling with GLAIP SDK.

Note: Commands below assume you run them from this folder unless noted otherwise.

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

3. **Run the example**

   ```bash
   uv run main.py
   ```

## Project Structure

```
programmatic-tool-calling/
├── tools/
│   └── __init__.py
├── main.py
├── pyproject.toml
└── .env.example
```
