"""Configuration and constants for the benchmark system.

Authors:
    Daniel Adi (daniel.adi@gdplabs.id)

"""

import os
from dataclasses import dataclass

try:
    from gllm_evals.evaluator.agent_evaluator import AgentEvaluator
    from gllm_evals.evaluator.geval_generation_evaluator import GEvalGenerationEvaluator
    from gllm_evals.types import RAGData

    GLLM_EVALS_AVAILABLE = True
    print("✅ gllm-evals successfully imported and available")
except ImportError as e:
    print(f"⚠️  gllm-evals not found: {e}")
    print(
        'Install with: pip install --extra-index-url "https://oauth2accesstoken:$(gcloud auth print-access-token)@glsdk.gdplabs.id/gen-ai-internal/simple/" "gllm-evals[deepeval,langchain,ragas]"'
    )
    GLLM_EVALS_AVAILABLE = False


@dataclass
class BenchmarkConfig:
    """Configuration for benchmark execution."""

    agent_id: str
    agent_timeout: float = 600.0  # Increased to handle concurrent load
    use_arun: bool = False
    backoff_time: float = 15.0  # Backoff between requests
    max_retry_duration: float = 300.0  # Max time for retries
    manual_review_auto_eval: bool = False

    openai_api_key: str | None = None
    evaluation_model: str = "gpt-4o-mini"

    workers: int = 1
    limit: int | None = None
    questions: list | None = None
    row_indices: list[int] | None = None  # Specific row numbers to process

    input_file: str = "input.csv"
    output_file: str | None = None

    api_url: str = os.getenv("AIP_API_URL", "https://beta-aip.obrol.id")
    api_key: str = os.getenv("AIP_API_KEY", "")

    def __post_init__(self):
        """Validate configuration after initialization."""
        if not self.api_key:
            raise ValueError("AIP_API_KEY environment variable must be set")

        if not self.api_url:
            self.api_url = "https://beta-aip.obrol.id"

        if not self.output_file:
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.output_file = f"test_evaluation_optimized_{timestamp}.csv"


DEFAULT_AGENT_TIMEOUT = 300.0
DEFAULT_EVALUATION_MODEL = "gpt-4o-mini"
DEFAULT_WORKERS = 1
MAX_CONTEXT_LENGTH = 20000
