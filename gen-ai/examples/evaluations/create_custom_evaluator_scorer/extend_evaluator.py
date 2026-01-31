"""
Custom Evaluator - Extending BaseEvaluator

This example demonstrates how to create a custom evaluator by extending
BaseEvaluator with your own evaluation logic.

Use this approach when:
- You need highly customized evaluation logic
- Built-in metrics don't fit your use case
- You have specific scoring requirements
"""

import asyncio
from gllm_evals.metrics.metric import BaseMetric
from gllm_evals.evaluator.evaluator import BaseEvaluator
from gllm_evals.types import MetricInput, MetricOutput, EvaluationOutput, QAData


class ExactMatchMetric(BaseMetric):
    """
    A custom metric that checks if the generated response exactly matches
    the expected response.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = "exact_match"

    async def _evaluate(self, data: MetricInput) -> MetricOutput:
        """Compare generated response with expected response."""
        score = int(data["generated_response"] == data["expected_response"])
        return {"score": score}


class ResponseEvaluator(BaseEvaluator):
    """
    A custom evaluator that uses the ExactMatchMetric.
    Demonstrates how to extend BaseEvaluator with your own logic.
    """

    def __init__(self) -> None:
        super().__init__(name="response_evaluator")
        self.metric = ExactMatchMetric()

    async def _evaluate(self, data: MetricInput) -> EvaluationOutput:
        """Evaluate the data using the custom metric."""
        return await self.metric.evaluate(data)


async def main() -> None:
    """Run the custom evaluator example."""
    data = QAData(
        query="What is the capital of France?",
        generated_response="The capital of France is Paris.",
        expected_response="The capital of France is Paris.",
    )

    evaluator = ResponseEvaluator()
    result = await evaluator.evaluate(data)
    print("Custom Evaluator Result (Extending BaseEvaluator):")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
