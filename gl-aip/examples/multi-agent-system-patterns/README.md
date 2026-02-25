# Multi-Agent System Patterns

This directory contains examples demonstrating various multi-agent system patterns using the GLAIP SDK.

## Available Patterns

- **Aggregator**: Agents contribute outputs that are collected and synthesized by an aggregator agent
- **Hierarchical**: Agents organized in a hierarchical structure with parent-child relationships
- **Loop**: Agents that iterate and refine outputs through multiple passes
- **Parallel**: Multiple agents execute simultaneously on different tasks
- **Router**: A central router determines which agent(s) to invoke based on the task
- **Sequential**: Tasks processed sequentially where one agent's output becomes the next agent's input

Each pattern includes a detailed README with examples and documentation. Navigate to the individual pattern directories for more information.

## Quick Start

```bash
cd python/gl-agents/projects/multi-agent-system-patterns
uv run <pattern-name>/main.py
```

Replace `<pattern-name>` with one of: `aggregator`, `hierarchical`, `loop`, `parallel`, `router`, or `sequential`.
