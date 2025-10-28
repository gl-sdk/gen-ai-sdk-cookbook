# BOSA MCP Example Project

This project demonstrates the usage of BOSA connectors and GLLM tools with the uv package manager.

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Setup

1. Clone or navigate to the project directory:
```bash
cd bosa-mcp
```

2. Install dependencies:
```bash
uv sync
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your BOSA credentials
```

## Configuration

Edit the `.env` file with your BOSA credentials:

```
BOSA_API_URL=https://your-bosa-api-url
BOSA_CLIENT_KEY=your-client-key
BOSA_IDENTIFIER=your-identifier
```

## Usage

Run the main script:
```bash
uv run main
```

## Dependencies

- `gllm-tools-binary` - GLLM tools for working with language models
- `bosa-connectors-binary` - BOSA connectors for data integration

## Project Structure

```
bosa-mcp/
├── main.py           # Main application script
├── pyproject.toml    # Project configuration and dependencies
├── .env.example      # Environment variable template
├── .env             # Environment variables (not in git)
├── README.md        # This file
└── uv.lock          # Dependency lock file
```

## Development

To add new dependencies:
```bash
uv add package-name
```

To update dependencies:
```bash
uv sync
```

