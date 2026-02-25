# Multi-Agent System Patterns

This directory contains examples for multi-agent system patterns using the GLAIP SDK.

## Available Patterns

- Aggregator: agents contribute outputs that are synthesized by an aggregator
- Hierarchical: parent-child agent relationships
- Loop: agents iterate and refine outputs through multiple passes
- Parallel: agents execute in parallel
- Router: a router agent selects the next best agent
- Sequential: outputs flow in a strict order from one agent to the next

Each pattern includes a dedicated README with details.

## Quick Start

```bash
cd examples/multi-agent-system-patterns
uv run <pattern-name>/main.py
```

Replace `<pattern-name>` with one of: `aggregator`, `hierarchical`, `loop`, `parallel`, `router`, or `sequential`.
