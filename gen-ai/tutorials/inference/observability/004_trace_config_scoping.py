"""Scope LM trace content capture to a single pipeline invocation with trace_config.

References:
    [1] https://gdplabs.gitbook.io/sdk/gen-ai-sdk/tutorials/inference/observability#capture-for-a-single-invocation
"""

import asyncio
from typing import TypedDict

from gllm_inference.observability import LMTraceContentConfig, get_lm_trace_content_config

from gllm_pipeline.pipeline import Pipeline
from gllm_pipeline.steps import transform


class DummyState(TypedDict):
    text: str
    input_text_captured: bool


def read_capture_flag(data: dict) -> bool:
    return get_lm_trace_content_config().input_text


async def main() -> None:
    """Show that trace_config scopes lm_trace_content to one invocation only."""
    pipeline = Pipeline(
        steps=[
            transform(
                read_capture_flag,
                input_map=["text"],
                output_state="input_text_captured",
                name="read_capture_flag",
            )
        ],
        state_type=DummyState,
    )

    result = await pipeline.invoke(
        {"text": "hello", "input_text_captured": False},
        thread_id="demo",
        trace_config={"lm_trace_content": LMTraceContentConfig(input_text=True, output_text=True)},
    )

    print("during invocation, input_text:", result["input_text_captured"])
    print("after invocation, input_text:", get_lm_trace_content_config().input_text)


if __name__ == "__main__":
    asyncio.run(main())
