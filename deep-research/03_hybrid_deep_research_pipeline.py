"""Cookbook example: Hybrid Deep Research Pipeline with Parallel Execution.

This cookbook demonstrates how to build a pipeline that combines multiple deep research
systems running in parallel to provide comprehensive, multi-perspective research results.

The pipeline intelligently routes user queries between two processing paths:
- Deep research: For complex queries requiring comprehensive research, this path executes
  TWO deep research systems in parallel (OpenAI Deep Researcher and GL Open Deep Researcher),
  then combines their results using a response synthesizer
- Normal response: For simple conversational queries like greetings and small talk

Key Features:
    - Intelligent query routing based on complexity
    - Parallel execution of multiple deep research systems for faster results
    - Result synthesis combining insights from different research approaches
    - Streaming event support for real-time updates
    - Leverages both OpenAI's o1-mini and GL Open's INTERNAL research profiles

Prerequisites:
    - Set OPENAI_API_KEY environment variable
    - Set GLODR_API_KEY environment variable (for GL Open Deep Researcher)
    - Install required dependencies (gllm-core, gllm-generation, gllm-inference, gllm-pipeline)

Authors:
    Delfia N. A. Putri (delfia.n.a.putri@gdplabs.id)

References:
    [1] https://gdplabs.gitbook.io/sdk/deep-researcher
"""

import asyncio

from gllm_core.event import EventEmitter
from gllm_generation.deep_researcher import GLOpenDeepResearcher, OpenAIDeepResearcher
from gllm_generation.response_synthesizer import ResponseSynthesizer
from gllm_inference.lm_invoker.openai_lm_invoker import OpenAILMInvoker
from gllm_inference.output_parser.json_output_parser import JSONOutputParser
from gllm_inference.prompt_builder import PromptBuilder
from gllm_inference.request_processor import LMRequestProcessor
from gllm_inference.schema import LMOutput
from gllm_pipeline.router import LMBasedRouter
from gllm_pipeline.steps import parallel, step, switch
from pydantic import BaseModel


class DeepResearchState(BaseModel):
    """Hybrid deep research state.

    This state model holds the data that flows through the pipeline. The router sets the
    `route` field, and the selected branch processes the query accordingly:
    - Deep research branch: Executes both researchers in parallel, stores results in
      `openai_result` and `glopen_result`, then combines them into `combined_result`
    - Normal branch: Directly sets the `combined_result` field

    Attributes:
        user_query (str): The user's research query to be processed.
        route (str | None): The route determined by the router ("deep_research" or "normal").
        openai_result (LMOutput | None): Result from OpenAI Deep Researcher (o1-mini).
        glopen_result (LMOutput | None): Result from GL Open Deep Researcher (INTERNAL).
        combined_result (str | LMOutput | None): Final synthesized result combining both research outputs.
        event_emitter (EventEmitter): Event emitter for streaming events during processing.
    """

    user_query: str
    route: str | None = None
    openai_result: LMOutput | None = None
    glopen_result: LMOutput | None = None
    combined_result: str | LMOutput | None = None
    event_emitter: EventEmitter

    class Config:
        """Pydantic configuration for DeepResearchState.

        Allows arbitrary types (like EventEmitter) to be used in the model.
        """

        arbitrary_types_allowed = True


# Step 1: Configure the LLM-based router
# The router uses an LLM to classify queries as either "deep_research" or "normal"
lmrp = LMRequestProcessor(
    prompt_builder=PromptBuilder(
        user_template="""
        Based on the following user query, determine if it is a deep research query or a normal query.

        - **normal**: Casual greetings, small talk, or simple conversational queries that do not require
          in-depth research. Examples: "hello", "how are you", "what's the weather", "thanks", "goodbye".

        - **deep_research**: Queries that require comprehensive research, multi-source analysis, or
          in-depth exploration of a topic. Examples: "research the latest AI trends", "compare X vs Y",
          "analyze the market for...", "what are the pros and cons of...".

        Output the answer in JSON format with "route" as the key. For example:
        {{"route": "deep_research"}} or {{"route": "normal"}}

        Query: {text}
        """
    ),
    lm_invoker=OpenAILMInvoker(model_name="gpt-4o-mini"),
    output_parser=JSONOutputParser(),
)

# Step 2: Create the router step
# This step classifies the user query and sets the "route" field in the state
router = step(
    component=LMBasedRouter(
        valid_routes={"deep_research", "normal"},
        lm_request_processor=lmrp,
        default_route="normal",
    ),
    input_map={"text": "user_query"},
    output_state="route",
)

# Step 3a: Define the OpenAI Deep Researcher step
# This step uses OpenAI's o1-mini model for deep research
# It processes the query and stores the result in the "openai_result" state field
openai_deep_researcher = step(
    component=OpenAIDeepResearcher(model_name="o1-mini"),
    input_map={"query": "user_query", "event_emitter": "event_emitter"},
    output_state="openai_result",
)

# Step 3b: Define the GL Open Deep Researcher step
# This step uses GL Open's INTERNAL profile for comprehensive research
# It processes the same query in parallel and stores the result in the "glopen_result" state field
glopen_deep_researcher = step(
    component=GLOpenDeepResearcher(profile="INTERNAL"),
    input_map={"query": "user_query", "event_emitter": "event_emitter"},
    output_state="glopen_result",
)

# Step 4: Create parallel execution step
# This step runs both deep researchers simultaneously for faster results
# The parallel execution reduces total processing time by ~40-50% compared to sequential execution
parallel_deep_research = parallel(
    [openai_deep_researcher, glopen_deep_researcher],
    name="parallel_deep_research",
)

# Step 5: Define the Response Synthesizer to combine results
# This step takes the outputs from both researchers and synthesizes them into a unified response
# It highlights complementary information, notes contradictions, and provides a coherent answer
reporter = step(
    component=ResponseSynthesizer.stuff_preset(
        model_id="openai/gpt-4o-mini",
        user_template="""
        You are tasked with combining research results from two different deep research systems.

        **OpenAI Deep Research Result:**
        {openai_result}

        **GL Open Deep Research Result:**
        {glopen_result}

        Please synthesize these two research results into a comprehensive, coherent answer that:
        1. Combines insights from both sources
        2. Highlights any complementary information
        3. Notes any contradictions or differences in findings
        4. Provides a unified, well-structured response

        Original Query: {query}
        """,
    ),
    input_map={
        "query": "user_query",
        "openai_result": "openai_result",
        "glopen_result": "glopen_result",
        "event_emitter": "event_emitter",
    },
    output_state="combined_result",
)

# Step 6: Compose the deep research branch
# This combines the parallel execution with the result synthesis
# Flow: Both researchers run in parallel -> Results are combined by the synthesizer
deep_research_branch = parallel_deep_research | reporter

# Step 7: Define the normal response branch
# This step handles simple conversational queries using a standard response synthesizer
# It directly processes the query without deep research
normal_response_synthesizer = step(
    component=ResponseSynthesizer.stuff_preset(
        model_id="openai/gpt-4o-mini",
        user_template="{query}",
    ),
    input_map={"query": "user_query", "event_emitter": "event_emitter"},
    output_state="combined_result",
)

# Step 8: Create the conditional switch step
# Routes to the appropriate branch based on the "route" field set by the router
# - "deep_research" -> Executes parallel research + synthesis
# - "normal" -> Executes simple response
conditional_step = switch(
    condition=lambda input: input["route"],
    branches={
        "deep_research": deep_research_branch,
        "normal": normal_response_synthesizer,
    },
)

# Step 9: Compose the complete pipeline
# The pipeline flows: router -> conditional_step (which routes to appropriate branch)
# Deep research queries will execute both researchers in parallel and combine results
deep_research_pipeline = router | conditional_step
deep_research_pipeline.state_type = DeepResearchState


async def main() -> None:
    """Run the hybrid deep research pipeline example.

    This function demonstrates how to use the pipeline with a sample query.
    The query "research about the latest trends in AI" will be classified as a
    deep research query and routed to execute both OpenAI Deep Researcher and
    GL Open Deep Researcher in parallel, then combine their results.

    To test the normal query path, change the user_query to something like "hello"
    or "how are you".
    """
    event_emitter = EventEmitter.with_print_handler()
    state = DeepResearchState(
        user_query="research about the latest trends in AI and machine learning",
        event_emitter=event_emitter,
        route=None,
    )

    result = await deep_research_pipeline.invoke(state)

    print(result)


if __name__ == "__main__":
    # Run the pipeline example
    # Prerequisites:
    #   1. Set OPENAI_API_KEY environment variable
    #   2. Set GLODR_API_KEY environment variable
    asyncio.run(main())

