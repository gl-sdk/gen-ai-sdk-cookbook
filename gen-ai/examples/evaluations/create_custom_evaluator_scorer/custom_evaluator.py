"""
Custom Evaluator - Combining Built-in Metrics

This example demonstrates how to use CustomEvaluator to combine
any set of built-in metrics for your evaluation needs.

Use this approach when:
- You can use existing metrics
- You want to mix and match built-in metrics
- You need a simple, quick solution
"""

import asyncio
import os
from dotenv import load_dotenv

from gllm_evals.evaluator.custom_evaluator import CustomEvaluator
from gllm_evals.metrics.retrieval.ragas_context_precision import (
    RagasContextPrecisionWithoutReference,
)
from gllm_evals.metrics.retrieval.ragas_context_recall import RagasContextRecall
from gllm_evals.types import RAGData

load_dotenv()


async def main() -> None:
    """Run the custom evaluator with built-in metrics example."""
    ragas_context_recall = RagasContextRecall(
        lm_model="openai/gpt-4.1",
        lm_model_credentials=os.getenv("OPENAI_API_KEY"),
    )

    ragas_context_precision = RagasContextPrecisionWithoutReference(
        lm_model="openai/gpt-4.1",
        lm_model_credentials=os.getenv("OPENAI_API_KEY"),
    )

    # Combine metrics into a custom evaluator
    evaluator = CustomEvaluator(
        metrics=[ragas_context_recall, ragas_context_precision],
        name="my_rag_evaluator",
    )

    data = RAGData(
        query="When was the first super bowl?",
        generated_response="The first superbowl was held on Jan 15, 1967",
        retrieved_context=[
            "The First AFL-NFL World Championship Game was an American football "
            "game played on January 15, 1967, at the Los Angeles Memorial Coliseum "
            "in Los Angeles."
        ],
        expected_response="The first superbowl was held on Jan 15, 1967",
    )

    result = await evaluator.evaluate(data)
    print("Custom Evaluator Result (Combining Built-in Metrics):")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
