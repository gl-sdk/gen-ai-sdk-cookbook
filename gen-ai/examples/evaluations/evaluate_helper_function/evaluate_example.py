"""
Evaluate Helper Function Example

This tutorial demonstrates how to use the `evaluate()` convenience helper function
that orchestrates the entire evaluation process from data loading to result tracking
in a single function call.

The evaluate() function supports:
- Structured evaluation rules (each record receives the same evaluation treatment)
- Multiple data sources (HuggingFace, Google Sheets, Langfuse, local files)
- Custom inference functions
- Multiple evaluators
- Experiment tracking
- Summary evaluators for aggregate metrics
"""

import asyncio
import os
from dotenv import load_dotenv

from gllm_evals import load_simple_qa_dataset
from gllm_evals.evaluate import evaluate
from gllm_evals.evaluator.geval_generation_evaluator import GEvalGenerationEvaluator
from gllm_evals.utils.shared_functionality import inference_fn

load_dotenv()


async def main() -> None:
    """Main function demonstrating the evaluate() helper."""
    results = await evaluate(
        # Load the built-in simple QA dataset
        data=load_simple_qa_dataset('.'),
        # Use the default inference function
        inference_fn=inference_fn,
        # Specify the evaluators to use
        evaluators=[
            GEvalGenerationEvaluator(
                model_credentials=os.getenv("GOOGLE_API_KEY")
            )
        ],
        # Optional: Add summary evaluators for aggregate metrics
        # summary_evaluators=[accuracy_summary],
    )
    print(results)


async def evaluate_with_custom_inference() -> None:
    """Example with a custom inference function."""
    from typing import Any

    def generate_response(row: dict[str, Any]) -> dict[str, Any]:
        """
        Custom inference function.

        Args:
            row: Dictionary containing input data (must include 'query' key)

        Returns:
            Dictionary with 'generated_response' key
        """
        query = row["user_query"]
        # Your inference logic here
        generated_response = f"Response to: {query}"
        return {"generated_response": generated_response}

    results = await evaluate(
        data=load_simple_qa_dataset(),
        inference_fn=generate_response,
        evaluators=[
            GEvalGenerationEvaluator(
                model_credentials=os.getenv("GOOGLE_API_KEY")
            )
        ],
    )
    print(results)


async def evaluate_with_google_sheets() -> None:
    """Example using Google Sheets as data source."""
    from langfuse import get_client
    from gllm_evals.dataset.spreadsheet_dataset import SpreadsheetDataset
    from gllm_evals.experiment_tracker.langfuse_experiment_tracker import (
        LangfuseExperimentTracker,
    )

    mapping = {
        "input": {
            "question_id": "question_id",
            "query": "query",
            "retrieved_context": "retrieved_context",
            "generated_response": "generated_response",
        },
        "expected_output": {"expected_response": "expected_response"},
        "metadata": {"topic": "topic"},
    }

    results = await evaluate(
        data=await SpreadsheetDataset.from_gsheets(
            sheet_id="YOUR_SHEET_ID",
            worksheet_name="test",
            client_email=os.getenv("GOOGLE_SHEETS_CLIENT_EMAIL"),
            private_key=os.getenv("GOOGLE_SHEETS_PRIVATE_KEY"),
        ),
        inference_fn=inference_fn,
        evaluators=[
            GEvalGenerationEvaluator(
                model_credentials=os.getenv("GOOGLE_API_KEY")
            )
        ],
        experiment_tracker=LangfuseExperimentTracker(
            langfuse_client=get_client(), mapping=mapping
        ),
    )
    print(results)


if __name__ == "__main__":
    # Run the basic example
    asyncio.run(main())

    # Uncomment to try other examples:
    # asyncio.run(evaluate_with_custom_inference())
    # asyncio.run(evaluate_with_google_sheets())
