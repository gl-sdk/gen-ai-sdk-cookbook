# Modular Tool Integration (Travel Assistant)

This example demonstrates how to build a complex agent that uses multiple tools organized across separate files and packages.

## Key Features
- **Modular Packaging**: The Weather tool is a full Python package (`weather/`) with internal helper files.
- **Standalone Tools**: Flight status, Stock checker, and Travel math tools are simple single-file implementations.
- **Agent Orchestration**: A single agent intelligently selects between these specialized tools.

## Structure
- `main.py`: The orchestration script.
- `tools/weather/`: A modular tool package with helper logic.
- `tools/flight_status.py`: Single-file tool example.
- `tools/stock_checker.py`: Single-file tool example.
- `tools/travel_math.py`: Single-file tool example.

## ⚙️ Prerequisites

Refer to the [main prerequisites documentation](../../README.md#️-prerequisites) for detailed setup requirements.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/GDP-ADMIN/gl-sdk-cookbook.git
cd gl-sdk-cookbook/glaip/examples/modular-tool-integration
```

### 2. Install Dependencies

```bash
uv sync
```

This command installs the GLAIP-SDK and other dependencies as specified in `pyproject.toml`.

For detailed GLAIP SDK installation instructions, see the [official installation guide](https://gdplabs.gitbook.io/gl-aip/gl-aip-sdk/get-started/install-and-configure).

### 3. Run the Example

```bash
uv run main.py
```
