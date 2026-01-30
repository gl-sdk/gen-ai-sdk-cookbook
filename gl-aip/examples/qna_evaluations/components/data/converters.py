"""Converters for transforming experiment tracker results to benchmark format.

Authors:
    Daniel Adi (daniel.adi@gdplabs.id)

"""

import json
from typing import Any

from rich.console import Console

from .csv_writer import format_tool_execution, format_context_items

console = Console()


def calculate_max_tools(df_results: Any) -> int:
    """Calculate maximum number of tools across all rows.
    
    Args:
        df_results: DataFrame from experiment tracker CSV
        
    Returns:
        Maximum number of tools found
    """
    max_tools = 0
    for _, row in df_results.iterrows():
        try:
            data_str = row.get("data", "{}")
            data_json = json.loads(data_str) if isinstance(data_str, str) else data_str
            metadata = data_json.get("_metadata", {})
            step_timings = metadata.get("step_timings", [])
            max_tools = max(max_tools, len(step_timings))
        except Exception:
            pass
    return max_tools


def extract_geval_data(geval_scores: list, result_idx: int, row: Any) -> dict[str, Any]:
    """Extract GEval evaluation data from scores list.
    
    Args:
        geval_scores: List of GEval score dictionaries
        result_idx: Current result index (1-based)
        row: DataFrame row with additional evaluation data
        
    Returns:
        Dictionary with evaluation metrics
    """
    eval_data = {}
    geval_data = geval_scores[result_idx - 1] if result_idx - 1 < len(geval_scores) else None
    
    if geval_data and isinstance(geval_data, dict):
        # Extract completeness
        completeness = geval_data.get("completeness", {})
        eval_data["geval_completeness"] = completeness.get("score") if isinstance(completeness, dict) else None
        eval_data["geval_completeness_explanation"] = completeness.get("explanation", "") if isinstance(completeness, dict) else ""
        
        # Extract groundedness
        groundedness = geval_data.get("groundedness", {})
        eval_data["geval_groundedness"] = groundedness.get("score") if isinstance(groundedness, dict) else None
        eval_data["geval_groundedness_explanation"] = groundedness.get("explanation", "") if isinstance(groundedness, dict) else ""
        
        # Extract redundancy
        redundancy = geval_data.get("redundancy", {})
        eval_data["geval_redundancy"] = redundancy.get("score") if isinstance(redundancy, dict) else None
        eval_data["geval_redundancy_explanation"] = redundancy.get("explanation", "") if isinstance(redundancy, dict) else ""
        
        # Extract language_consistency
        language_consistency = geval_data.get("language_consistency", {})
        eval_data["geval_language_consistency"] = language_consistency.get("score") if isinstance(language_consistency, dict) else None
        eval_data["geval_language_consistency_explanation"] = language_consistency.get("explanation", "") if isinstance(language_consistency, dict) else ""
        
        # Extract refusal_alignment
        refusal_alignment = geval_data.get("refusal_alignment", {})
        eval_data["geval_refusal_alignment"] = refusal_alignment.get("score") if isinstance(refusal_alignment, dict) else None
        eval_data["geval_refusal_alignment_explanation"] = refusal_alignment.get("explanation", "") if isinstance(refusal_alignment, dict) else ""
        
        # Extract auto_rr and possible_issues
        eval_data["auto_rr"] = geval_data.get("relevancy_rating")
        geval_issues = geval_data.get("possible_issues", [])
        
        # Check artifact validation from evaluation results
        artifact_issues = []
        if row.get("artifact_validation.score") == False or row.get("artifact_validation.score") == "False":
            artifact_issues.append("Visualization required but no artifacts generated")
        
        # Merge all possible issues
        all_issues = list(geval_issues) + artifact_issues
        eval_data["possible_issues"] = ", ".join(all_issues) if all_issues else ""
    else:
        # No GEval data available
        eval_data["geval_completeness"] = None
        eval_data["geval_completeness_explanation"] = ""
        eval_data["geval_groundedness"] = None
        eval_data["geval_groundedness_explanation"] = ""
        eval_data["geval_redundancy"] = None
        eval_data["geval_redundancy_explanation"] = ""
        eval_data["geval_language_consistency"] = None
        eval_data["geval_language_consistency_explanation"] = ""
        eval_data["geval_refusal_alignment"] = None
        eval_data["geval_refusal_alignment_explanation"] = ""
        eval_data["auto_rr"] = None
        eval_data["possible_issues"] = ""
    
    return eval_data


def process_experiment_row(
    row: Any,
    result_idx: int,
    max_tools: int,
    manual_review_auto_eval: bool,
    geval_scores: list,
) -> dict[str, Any]:
    """Process a single experiment tracker row into result format.
    
    Args:
        row: DataFrame row from experiment tracker
        result_idx: Result index (1-based)
        max_tools: Maximum number of tools to pre-allocate columns
        manual_review_auto_eval: Whether to use detailed manual review columns
        geval_scores: List of GEval score dictionaries
        
    Returns:
        Dictionary with result row data
    """
    # Parse JSON from 'data' column
    data_json = {}
    try:
        data_str = row.get("data", "{}")
        if isinstance(data_str, str):
            data_json = json.loads(data_str)
        elif isinstance(data_str, dict):
            data_json = data_str
    except Exception as e:
        console.print(f"[yellow]Warning: Could not parse data JSON: {e}[/yellow]")
    
    # Extract metadata
    metadata = data_json.get("_metadata", {})
    
    # Build base result row in NEW format
    result_row = {
        "Index": result_idx,
        "Question": data_json.get("query", ""),
        "Expected Answer": data_json.get("expected_response", ""),
        "Answer": data_json.get("generated_response", ""),
        "Response_Time": metadata.get("execution_time", 0) if isinstance(metadata, dict) else 0,
        "sources": metadata.get("sources", "") if isinstance(metadata, dict) else "",
        "retrieved_context": json.dumps(metadata.get("retrieved_context", [])) if isinstance(metadata, dict) else "[]",
        "steps": json.dumps(metadata.get("step_timings", [])) if isinstance(metadata, dict) else "[]",
        "thinking_steps": "\n\n".join([s.get("content", "") for s in metadata.get("thinking_steps", []) if isinstance(s, dict)]) if isinstance(metadata, dict) else "",
        "artifacts": json.dumps(data_json.get("artifacts", [])),
        "agent_error": metadata.get("error", "") if isinstance(metadata, dict) else "",
        "evaluation_error": "",
        "timeout_debug_info": "",
    }
    
    # Add manual review columns if needed
    if manual_review_auto_eval:
        result_row.update({
            "manual_review_answer_relevance": "",
            "manual_review_answer_quality": "",
            "manual_review_context_quality": "",
            "manual_review_notes": "",
        })
    
    # Add evaluation metrics
    eval_data = extract_geval_data(geval_scores, result_idx, row)
    result_row.update(eval_data)
    
    return result_row


def convert_experiment_tracker_results(
    df_results: Any,
    manual_review_auto_eval: bool = False,
    geval_scores: list[dict[str, Any] | None] = None,
) -> list[dict[str, Any]]:
    """Convert experiment tracker CSV results to benchmark CSV format.
    
    Args:
        df_results: DataFrame from experiment tracker CSV
        manual_review_auto_eval: Whether to use detailed manual review columns
        geval_scores: List of GEval score dictionaries from evaluation_result["results"]
    
    Returns:
        List of result dictionaries for CSV output
    """
    geval_scores = geval_scores or []
    
    # Calculate max tools across all rows
    max_tools = calculate_max_tools(df_results)
    console.print(f"📊 Max tools found across all rows: {max_tools}")
    
    # Process each row
    results = []
    for result_idx, (df_idx, row) in enumerate(df_results.iterrows(), 1):
        result_row = process_experiment_row(
            row=row,
            result_idx=result_idx,
            max_tools=max_tools,
            manual_review_auto_eval=manual_review_auto_eval,
            geval_scores=geval_scores,
        )
        results.append(result_row)
    
    return results
