"""Evaluation module for agent benchmarking.

This module contains evaluators, metrics, and wrappers for comprehensive agent evaluation.

Authors:
    Daniel Adi (daniel.adi@gdplabs.id)

"""

from .evaluator import ComprehensiveAgentEvaluator
from .wrappers import LoggingEvaluatorWrapper

# Import ArtifactValidationMetric conditionally since it requires gllm_evals
try:
    from .metrics import ArtifactValidationMetric
    __all__ = [
        "ComprehensiveAgentEvaluator",
        "ArtifactValidationMetric",
        "LoggingEvaluatorWrapper",
    ]
except ImportError:
    __all__ = [
        "ComprehensiveAgentEvaluator",
        "LoggingEvaluatorWrapper",
    ]
    ArtifactValidationMetric = None
