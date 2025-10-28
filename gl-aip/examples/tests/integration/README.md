## ⚙️ Prerequisites

Refer to the [main prerequisites documentation](../../../README.md#️-prerequisites) for detailed setup requirements.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
cd gen-ai-sdk-cookbook/gl-aip/examples/tests/integration
```

### 2. Install Dependencies

```bash
uv sync
```

This command installs the GL AIP as specified in `pyproject.toml`.

For detailed GL AIP installation instructions, see the [official installation guide](https://gdplabs.gitbook.io/gl-aip/gl-aip-sdk/get-started/install-and-configure).

### 3. Configure Environment Variables

Copy the example environment file and set your values:

```bash
# Copy .env.example to .env
cp .env.example .env
```

Then edit the `.env` file and set the values with your actual AIP API URL and AIP API key.

> **Note:** The `.env` file contains sensitive information and should not be committed to version control.

### 4. Run the Example

```bash
uv run pytest main.py -v
# or
uv run pytest main.py -v -s  # (for debug)
```

### 5. Expected Output

Upon successful execution, you should see output similar to:

```
=========================================== test session starts ===========================================
platform darwin -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0 -- /Users/reinhart.linanda/Projects/gen-ai-sdk-cookbook/gl-aip/examples/tests/integration/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/reinhart.linanda/Projects/gen-ai-sdk-cookbook/gl-aip/examples/tests/integration
configfile: pyproject.toml
plugins: anyio-4.11.0
collected 1 item

main.py::TestCalendarAssistantAgent::test_calendar_assistant_agent[Schedule an interview] PASSED    [100%]

=========================================== 1 passed in 10.39s ============================================
```

## 📚 Reference

This example is based on the [Auto Check Tool](https://github.com/GDP-ADMIN/glaip-sdk/tree/bbfeb3ea5a0c095c843c34a77e753f6832bd86c7/python/glaip-sdk/examples/auto_check_tool).
