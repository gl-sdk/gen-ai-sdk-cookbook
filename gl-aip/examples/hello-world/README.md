## ⚙️ Prerequisites

Refer to the [main prerequisites documentation](../../README.md#️-prerequisites) for detailed setup requirements.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
cd gen-ai-sdk-cookbook/gl-aip/examples/hello-world
```

### 2. Install Dependencies

```bash
uv sync
```

This command installs the GL AIP as specified in `pyproject.toml`.

For detailed GL AIP installation instructions, see the [official installation guide](https://gdplabs.gitbook.io/gl-aip/gl-aip-sdk/get-started/install-and-configure).

### 3. Run the Example

```bash
uv run main.py
```

### 4. Expected Output

Upon successful execution, you should see output similar to:

```
───────────────────────────────────────────── 🤖 hello-world-agent ─────────────────────────────────────────────
 ──────────────────────────────────────────────── User Request ────────────────────────────────────────────────
  Query: Hello! How are you today?
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ─────────────────────────────────────────────────── Steps ────────────────────────────────────────────────────
  No steps yet
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ──────────────────────────────────────────────── Final Result ────────────────────────────────────────────────
  Hello! I'm just a virtual assistant, so I don't have feelings, but I'm here and ready to help you. How can I
  assist you today? 😊
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

## 📚 Reference

This example is based on the [GL AIP Quick Start Guide](https://gdplabs.gitbook.io/gl-aip/getting-started/quick-start-guide).