import json

import pytest
from gllm_evals.types import MetricInput

from load_dataset import load_dataset
from metrics.sql_result_assertion import SQLResultAssertionMetric
from gllm_evals.metrics.generation.geval_groundedness import GEvalGroundednessMetric

DATASET_PATH = "sample_dataset_v2.json"
PASSING_SCORE = 2  # score >= 2 on a 1-3 scale equals the 0.67 threshold

_dataset = load_dataset(DATASET_PATH)


def _entry_id(row: dict) -> str:
    return f"entry_{row.get('id', 'unknown')}"


@pytest.mark.parametrize("row", _dataset, ids=[_entry_id(r) for r in _dataset])
async def test_sql_assertion(
    row: dict,
    metric: GEvalGroundednessMetric,
    record_result,
) -> None:
    ground_truth_data = row.get("ground_truth")
    entry_id = _entry_id(row)

    if not ground_truth_data:
        record_result({
            "id": entry_id,
            "question": row.get("input", ""),
            "status": "skipped",
            "reason": "No retrieved_context (SQL results) available",
        })
        pytest.skip("No retrieved_context (SQL results) available")

    # Convert SQL results (list of dicts) to list of strings
    retrieved_context = [json.dumps(item) for item in ground_truth_data]

    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
    # Result can be a dict or MetricOutput object
    score = result['geval_groundedness'].get("score")
    explanation = result['geval_groundedness'].get("explanation", "")

    record_result({
        "id": entry_id,
        "question": row.get("input", ""),
        "status": "passed" if (score is not None and score >= PASSING_SCORE) else "failed",
        "score": score,
        "explanation": explanation,
    })

    assert score is not None, "Metric returned no score"
    assert score >= PASSING_SCORE, (
        f"Score {score}/3 is below passing threshold ({PASSING_SCORE}/3)\n"
        f"Question: {row.get('input', '')[:120]}\n"
        f"Explanation: {explanation}"
    )
