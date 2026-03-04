# Programmatic Tool Calling

This cookbook includes:

- `main_with_mcp.py`: PTC baseline with MCP integration
- `main_without_ptc.py`: standard tool calling
- `main_with_ptc.py`: Programmatic Tool Calling (PTC) with `execute_ptc_code`
- `compare_runs_budget.py`: single-file benchmark on large raw tool output

It shows that you can use both at the same time in one agent:

- MCP tools via `mcps=[...]`
- custom LangChain tools via `tools=[...]`

The core comparison uses the same customer-support question in two modes:


Scenario:

> "What did Alice order recently, and what's her email so I can follow up?"

The answer requires **two dependent tool calls**:

1. `get_user(name)` -> returns user profile (including `id`)
2. `get_orders(user_id)` -> uses that returned `id`

Both tools are mocked LangChain `BaseTool` classes (`tools/get_user_tool.py` and `tools/get_orders_tool.py`). Each file is self-contained and returns a consistent shape:

```json
{
  "status": "ok | not_found",
  "message": "...",
  "data": {}
}
```

Note: Commands below assume you run them from this folder unless noted otherwise.

## Quick Start

1. Setup environment

   ```bash
   cp .env.example .env
   # Edit .env with OPENAI_API_KEY
   # Add E2B_API_KEY when running the PTC script
   ```

2. Install dependencies

   ```bash
   uv sync
   ```

3. Run PTC + MCP baseline

   ```bash
   uv run python main_with_mcp.py
   ```

4. Run without PTC

   ```bash
   uv run python main_without_ptc.py
   ```

5. Run with PTC

   ```bash
   uv run python main_with_ptc.py
   ```

6. Compare on large raw tool outputs (budget audit scenario)

   ```bash
   uv run python compare_runs_budget.py
   ```

   This scenario is intentionally built to favor PTC by returning large raw expense line-items,
   so code execution can aggregate totals before the final answer. It prints duration,
   wall time, token usage, and LLM step count. The non-PTC run is constrained to one
   tool call per turn so round-trip overhead is visible.

   Edit variables at the top of `compare_runs_budget.py` if needed:

   - `QUERY`
   - `RUNS`
   - `SHOW_RESPONSES`

## When PTC Helps (and when not)

PTC is usually beneficial when orchestration is non-trivial:

- many dependent tool calls (step B needs step A output)
- large raw tool payloads that should be pre-aggregated/filter in code
- workflows with loops, conditional branches, and explicit error handling
- cases where reducing LLM round-trips is important

PTC may be unnecessary for simple tasks:

- one small tool call with minimal post-processing
- short two-step flows where normal tool calling is already clear and fast
- scenarios where sandbox startup/exec overhead is larger than orchestration gain

## Project Structure

```
programmatic-tool-calling/
├── tools/
│   ├── __init__.py
│   ├── get_user_tool.py
│   └── get_orders_tool.py
├── main_with_mcp.py
├── main_without_ptc.py
├── main_with_ptc.py
├── compare_runs_budget.py
├── tools_budget/
│   ├── __init__.py
│   ├── get_team_members_tool.py
│   ├── get_expenses_tool.py
│   └── get_budget_by_level_tool.py
├── pyproject.toml
└── .env.example
```
