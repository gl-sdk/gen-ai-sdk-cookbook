# Hierarchical Pattern

Agents are organized in a tree-like structure, with higher-level agents (supervisor agents) managing lower-level ones.

## Demo Scenario: Multi-level Research System

This example demonstrates a hierarchical agent system with three levels:

- **Coordinator**: Orchestrates the workflow and communicates with user
- **Research Agent**: Performs web searches using web_search_tool
- **Information Compiler**: Formats and synthesizes research results

The flow follows: Coordinator -> Research Agent -> Coordinator -> Information Compiler -> Coordinator -> User

In the demo, the system researches "Latest developments in artificial intelligence for healthcare in 2025" by delegating the web search to the research agent, then passing the results to the information compiler for formatting, before presenting the final results to the user.

## Quick Start

```bash
cd python/gl-agents/projects/multi-agent-system-patterns
uv run hierarchical/main.py
```

## Documentation

See the [Hierarchical Pattern](https://glaip-sdk.gitbook.io/docs/how-to-guides/multi-agent-system-patterns/hierarchical) guide for full documentation.
