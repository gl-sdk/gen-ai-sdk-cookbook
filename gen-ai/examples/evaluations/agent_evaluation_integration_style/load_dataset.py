import json
from pathlib import Path
from typing import Any


def load_dataset(file_path: str | Path) -> list[dict[str, Any]]:
    """Load and parse a JSON dataset containing agent evaluation data.

    Args:
        file_path: Path to the JSON file to load.

    Returns:
        List of dictionaries containing the parsed dataset entries.
        Each entry may contain keys: "input", "response", "trajectory",
        "ground_truth".

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        return [data]
    elif isinstance(data, list):
        return data
    else:
        raise ValueError(f"Expected JSON object or array, got {type(data).__name__}")


def parse_dataset_entry(entry: dict[str, Any]) -> dict[str, Any]:
    """Parse a single dataset entry and extract relevant fields.

    Args:
        entry: Dictionary containing the dataset entry.

    Returns:
        Dictionary with parsed fields: "id", "input", "response", "trajectory",
        "ground_truth".
        Missing fields will have None values.
    """
    return {
        "id": entry.get("id"),
        "input": entry.get("input"),
        "response": entry.get("response"),
        "trajectory": entry.get("trajectory"),
        "ground_truth": entry.get("ground_truth"),
    }
