## ⚙️ Prerequisites

Refer to the [main prerequisites documentation](../../README.md#️-prerequisites) for detailed setup requirements.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/gl-sdk/gen-ai-sdk-cookbook.git
cd gen-ai-sdk-cookbook/glaip/examples/runtime-config
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
───────────────────────────────────────────────────────────────────── 🤖 bosa-sql-query-agent ──────────────────────────────────────────────────────────────────────
 ────────────────────────────────────────────────────────────────────────── User Request ──────────────────────────────────────────────────────────────────────────
  Query: How many tables are in the database?
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ───────────────────────────────────────────────────────────────────────────── Steps ──────────────────────────────────────────────────────────────────────────────
  ⚙️ bosa_sql_query_tool [3.26s] ✓
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ──────────────────────────────────────────────────────────────── Bosa Sql Query Tool  · 3.26s  ✓ ─────────────────────────────────────────────────────────────────
  Args:


   {
     "query": "SELECT COUNT(*) as table_count FROM information_schema.tables WHERE table_schema = 'public';"
   }


  Output: [{'table_count': 0}]
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ────────────────────────────────────────────────────────────────────────── Final Result ──────────────────────────────────────────────────────────────────────────
  There are currently no tables in the database. If you need help creating tables or have other questions, please let me know!
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```
