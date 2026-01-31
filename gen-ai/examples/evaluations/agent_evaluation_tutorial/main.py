"""Example of using the AgentEvaluator.
"""

import asyncio
import json

from gllm_evals.dataset import load_simple_agent_tool_call_dataset
from gllm_evals.evaluator.agent_evaluator import AgentEvaluator


async def main():
    """Main function."""
    data = load_simple_agent_tool_call_dataset()

    evaluator = AgentEvaluator()

    result = await evaluator.evaluate(data[0])
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
