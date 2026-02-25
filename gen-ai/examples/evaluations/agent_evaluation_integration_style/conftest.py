import csv
import os
from datetime import datetime
from pathlib import Path

import pytest
from dotenv import load_dotenv

from metrics.sql_result_assertion import SQLResultAssertionMetric
from gllm_evals.metrics.generation.geval_groundedness import GEvalGroundednessMetric

_run_results: list[dict] = []


@pytest.fixture(scope="session")
def metric() -> GEvalGroundednessMetric:
    load_dotenv()
    return GEvalGroundednessMetric(
        model_credentials=os.getenv("GOOGLE_API_KEY"),
        threshold=0.67,  # 2/3 on a 1-3 scale
    )


@pytest.fixture
def record_result():
    """Return a callable that appends a result entry to the run log."""
    def _record(entry: dict) -> None:
        _run_results.append(entry)
    return _record


def pytest_sessionfinish(session, exitstatus):
    """Write all collected results to a timestamped CSV file after the run."""
    if not _run_results:
        return
    Path("runs").mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    output_path = Path("runs") / f"run_{timestamp}.csv"
    fieldnames = list(_run_results[0].keys())
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(_run_results)
    print(f"\nResults saved to: {output_path}")
