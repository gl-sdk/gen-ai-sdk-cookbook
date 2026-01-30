"""Converter for building result rows directly from inference data.

Authors:
    Daniel Adi (daniel.adi@gdplabs.id)

"""

import json
from typing import Any

from rich.console import Console

console = Console()


def build_result_row_from_inference(
    idx: int,
    data_item: dict[str, Any],
    enriched_data: dict[str, Any],
    manual_review_auto_eval: bool = False,
) -> dict[str, Any]:
    """Build result row directly from inference data without evaluation.
    
    Args:
        idx: Row index (0-based)
        data_item: Original data item with query, expected_answer, etc.
        enriched_data: Enriched data from inference_fn with answer, sources, etc.
        manual_review_auto_eval: Whether to include manual review columns
        
    Returns:
        Dictionary with result row data
    """
    # Extract metadata (create_inference_fn stores most data in _metadata)
    metadata = enriched_data.get("_metadata", {})
    
    result_row = {
        "Index": idx + 1,
        "Question": data_item.get("query", ""),
        "Expected Answer": data_item.get("expected_answer", ""),
        "Answer": enriched_data.get("generated_response", ""),
        "Response_Time": metadata.get("execution_time", 0),
        "sources": metadata.get("sources", ""),
        "retrieved_context": json.dumps(metadata.get("retrieved_context", [])),
        "steps": json.dumps(metadata.get("step_timings", [])),
        "thinking_steps": "\n\n".join([s.get("content", "") for s in metadata.get("thinking_steps", []) if isinstance(s, dict)]),
        "artifacts": json.dumps(enriched_data.get("artifacts", [])),
        "agent_error": metadata.get("error", ""),
        "evaluation_error": "",
        "timeout_debug_info": "",
    }
    
    if manual_review_auto_eval:
        result_row.update({
            "manual_review_answer_relevance": "",
            "manual_review_answer_quality": "",
            "manual_review_context_quality": "",
            "manual_review_notes": "",
        })
    
    return result_row
