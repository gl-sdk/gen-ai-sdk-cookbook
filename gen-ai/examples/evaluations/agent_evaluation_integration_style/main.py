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


@pytest.mark.parametrize("row", [_dataset[0]], ids=[_entry_id(_dataset[0])])
async def test_sql_assertion_0(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[1]], ids=[_entry_id(_dataset[1])])
async def test_sql_assertion_1(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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
    assert score <= 1, (
        f"Score {score}/3 is above expected max threshold (1/3)\n"
        f"Question: {row.get('input', '')[:120]}\n"
        f"Explanation: {explanation}"
    )


@pytest.mark.parametrize("row", [_dataset[2]], ids=[_entry_id(_dataset[2])])
async def test_sql_assertion_2(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[3]], ids=[_entry_id(_dataset[3])])
async def test_sql_assertion_3(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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
    assert score <= 1, (
        f"Score {score}/3 is above expected max threshold (1/3)\n"
        f"Question: {row.get('input', '')[:120]}\n"
        f"Explanation: {explanation}"
    )


@pytest.mark.parametrize("row", [_dataset[4]], ids=[_entry_id(_dataset[4])])
async def test_sql_assertion_4(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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
    assert score <= 1, (
        f"Score {score}/3 is above expected max threshold (1/3)\n"
        f"Question: {row.get('input', '')[:120]}\n"
        f"Explanation: {explanation}"
    )


@pytest.mark.parametrize("row", [_dataset[5]], ids=[_entry_id(_dataset[5])])
async def test_sql_assertion_5(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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
    assert score <= 1, (
        f"Score {score}/3 is above expected max threshold (1/3)\n"
        f"Question: {row.get('input', '')[:120]}\n"
        f"Explanation: {explanation}"
    )


@pytest.mark.parametrize("row", [_dataset[6]], ids=[_entry_id(_dataset[6])])
async def test_sql_assertion_6(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[7]], ids=[_entry_id(_dataset[7])])
async def test_sql_assertion_7(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[8]], ids=[_entry_id(_dataset[8])])
async def test_sql_assertion_8(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[9]], ids=[_entry_id(_dataset[9])])
async def test_sql_assertion_9(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[10]], ids=[_entry_id(_dataset[10])])
async def test_sql_assertion_10(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[11]], ids=[_entry_id(_dataset[11])])
async def test_sql_assertion_11(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[12]], ids=[_entry_id(_dataset[12])])
async def test_sql_assertion_12(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[13]], ids=[_entry_id(_dataset[13])])
async def test_sql_assertion_13(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[14]], ids=[_entry_id(_dataset[14])])
async def test_sql_assertion_14(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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


@pytest.mark.parametrize("row", [_dataset[15]], ids=[_entry_id(_dataset[15])])
async def test_sql_assertion_15(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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
    assert score <= 1, (
        f"Score {score}/3 is above expected max threshold (1/3)\n"
        f"Question: {row.get('input', '')[:120]}\n"
        f"Explanation: {explanation}"
    )


@pytest.mark.parametrize("row", [_dataset[16]], ids=[_entry_id(_dataset[16])])
async def test_sql_assertion_16(row: dict, metric: GEvalGroundednessMetric, record_result) -> None:
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

    retrieved_context = [json.dumps(item) for item in ground_truth_data]
    data: MetricInput = {
        "query": row.get("input", ""),
        "generated_response": row.get("response", ""),
        "retrieved_context": retrieved_context,
    }

    result = await metric.evaluate(data)
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
