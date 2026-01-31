"""Example of using the AgentEvaluator with LangChain Agent Trajectory Accuracy metric.

This example demonstrates how to use the AgentEvaluator with the optional
LangChainAgentTrajectoryAccuracyMetric enabled. The trajectory accuracy metric
evaluates the agent's trajectory using LangChain's agentevals approach.
"""

import asyncio
import json
import os

from gllm_evals.constant import DefaultValues
from gllm_evals.dataset import load_simple_agent_tool_call_dataset
from gllm_evals.evaluator.agent_evaluator import AgentEvaluator
from gllm_evals.metrics.agent.langchain_agent_trajectory_accuracy import (
    LangChainAgentTrajectoryAccuracyMetric,
)


async def main():
    """Main function demonstrating AgentEvaluator with trajectory accuracy metric."""
    data = load_simple_agent_tool_call_dataset()

    # Configure the trajectory accuracy metric (optional)
    # This metric will only run when agent_trajectory is present in the input data
    trajectory_accuracy = LangChainAgentTrajectoryAccuracyMetric(
        model=DefaultValues.AGENT_EVALS_MODEL,
        model_credentials=os.getenv("OPENAI_API_KEY"),
    )

    # Create evaluator with both metrics
    evaluator = AgentEvaluator(
        trajectory_accuracy_metric=trajectory_accuracy,
    )

    # Evaluate the first data item
    result = await evaluator.evaluate(data[1])

    print("Evaluation Result:")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
