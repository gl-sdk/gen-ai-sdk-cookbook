"""Scope LM trace content capture to a single LMInvoker.invoke call with trace_config.

References:
    [1] https://gdplabs.gitbook.io/sdk/gen-ai-sdk/tutorials/inference/observability#capture-for-a-single-invocation
"""

import asyncio

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

from gllm_inference.lm_invoker import OpenAILMInvoker
from gllm_inference.model import OpenAILM
from gllm_inference.observability import LMTraceContentConfig

exporter = InMemorySpanExporter()
provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(exporter))
trace.set_tracer_provider(provider)

CONTENT_ATTRIBUTES = (
    "gen_ai.system_instructions",
    "gen_ai.input.messages",
    "gen_ai.output.messages",
)


def captured_content_keys() -> list[str]:
    """Return the content keys on the finished spans, then clear the exporter."""
    provider.force_flush()
    keys: set[str] = set()
    for span in exporter.get_finished_spans():
        keys |= {key for key in CONTENT_ATTRIBUTES if key in (span.attributes or {})}
    exporter.clear()
    return sorted(keys)


async def main() -> None:
    """Show that trace_config scopes lm_trace_content to one invocation only."""
    lm_invoker = OpenAILMInvoker(OpenAILM.GPT_5_NANO)
    scoped = LMTraceContentConfig(input_text=True, output_text=True)
    try:
        await lm_invoker.invoke(
            "What is the capital of France?",
            trace_config={"lm_trace_content": scoped},
        )
        print("with trace_config:", captured_content_keys())

        await lm_invoker.invoke("What is the capital of France?")
        print("without trace_config:", captured_content_keys())
    finally:
        await lm_invoker.release_resources()


if __name__ == "__main__":
    asyncio.run(main())
