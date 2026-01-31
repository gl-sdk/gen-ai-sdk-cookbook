# Agent Evaluation Tutorial

This tutorial demonstrates how to evaluate AI agents using the GenAI Evaluator SDK.

## Quick Start

### 1. Install Dependencies

```bash
make install
```

### 2. Set Up Environment

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run the Examples

```bash
make run              # Run basic agent evaluation
make run-trajectory  # Run agent evaluation with trajectory accuracy
```

## Tutorial Contents

### Example 1: Basic Agent Evaluation

**Run:** `make run`

This example demonstrates basic agent evaluation using `AgentEvaluator`:

```python
from gllm_evals.dataset import load_simple_agent_tool_call_dataset
from gllm_evals.evaluator.agent_evaluator import AgentEvaluator

data = load_simple_agent_tool_call_dataset()
evaluator = AgentEvaluator()
result = await evaluator.evaluate(data[0])
```

The evaluator checks:
- Tool call correctness
- Parameter accuracy
- Response relevance

### Example 2: Agent Evaluation with Trajectory Accuracy

**Run:** `make run-trajectory`

This example demonstrates agent evaluation with trajectory accuracy using `LangChainAgentTrajectoryAccuracyMetric`:

```python
from gllm_evals.metrics.agent.langchain_agent_trajectory_accuracy import (
    LangChainAgentTrajectoryAccuracyMetric,
)

trajectory_accuracy = LangChainAgentTrajectoryAccuracyMetric(
    model=DefaultValues.AGENT_EVALS_MODEL,
    model_credentials=os.getenv("OPENAI_API_KEY"),
)

evaluator = AgentEvaluator(
    trajectory_accuracy_metric=trajectory_accuracy,
)
```

The trajectory accuracy metric evaluates:
- Agent's decision path
- Tool selection correctness
- Sequential reasoning quality

## Output Format

```json
{
  "agent_evaluator": {
    "global_explanation": "Summary of evaluation results",
    "tool_call_accuracy": {
      "score": 1.0,
      "explanation": "All tool calls were correct"
    },
    "trajectory_accuracy": {
      "score": 0.85,
      "explanation": "Agent followed optimal path"
    }
  }
}
```

## Data Format

The agent evaluation requires agent trajectory data:

| Field | Description |
|-------|-------------|
| `query` | User input/question |
| `agent_trajectory` | Agent's execution path (optional) |
| `tool_calls` | List of tools called |
| `final_response` | Agent's final response |

## Available Make Commands

```bash
make install         # Install dependencies
make run             # Run basic agent evaluation
make run-trajectory  # Run agent evaluation with trajectory accuracy
make clean           # Clean up generated files
```

## Further Reading

- [Getting Started](../getting_started/) - Basic evaluation concepts
- [Create Custom Evaluator](../create_custom_evaluator_scorer/) - Custom evaluator guide
- [Multiple LLM-as-a-Judge](../multiple_llm_as_a_judge/) - Using multiple judges
