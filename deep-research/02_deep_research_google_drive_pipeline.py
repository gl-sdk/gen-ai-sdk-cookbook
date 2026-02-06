"""Cookbook example: Deep Research Pipeline with Router and Google Drive Integration.

This cookbook demonstrates how to build a pipeline that intelligently routes user queries
between two processing paths:
- Deep research: For complex queries requiring comprehensive research and multi-source analysis
  (with Google Drive connectivity for accessing documents)
- Normal response: For simple conversational queries like greetings and small talk

The pipeline uses an LLM-based router to classify queries, then routes them to the appropriate
processor. The deep research branch includes Google Drive integration, allowing the researcher
to access and analyze documents stored in Google Drive during the research process.

Key Features:
    - Intelligent query routing based on complexity
    - Google Drive connector for accessing documents during deep research
    - Streaming event support for real-time updates

Prerequisites:
    - Set OPENAI_API_KEY environment variable
    - Configure Google Drive authentication token (replace <google_drive_auth_token> placeholder)
      See: https://platform.openai.com/docs/guides/tools-connectors-mcp?quickstart-panels=connector#authorizing-a-connector
      Required OAuth scopes: userinfo.email, userinfo.profile, drive.readonly
    - Install required dependencies (gllm-core, gllm-generation, gllm-inference, gllm-pipeline)

Authors:
    Surya Mahadi (made.r.s.mahadi@gdplabs.id)

References:
    [1] https://gdplabs.gitbook.io/sdk/tutorials/generation/deep-researcher
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_core.event import EventEmitter
from gllm_generation.deep_researcher import OpenAIDeepResearcher
from gllm_generation.response_synthesizer import ResponseSynthesizer
from gllm_inference.lm_invoker.openai_lm_invoker import OpenAILMInvoker
from gllm_inference.output_parser.json_output_parser import JSONOutputParser
from gllm_inference.prompt_builder import PromptBuilder
from gllm_inference.request_processor import LMRequestProcessor
from gllm_inference.schema import LMOutput, NativeTool
from gllm_pipeline.router import LMBasedRouter
from gllm_pipeline.steps import step, switch
from pydantic import BaseModel

load_dotenv()


class DeepResearchState(BaseModel):
    """Deep research state.

    This state model holds the data that flows through the pipeline. The router sets the
    `route` field, and the selected branch (deep_researcher or normal_response_synthesizer)
    sets the `result` field.

    Attributes:
        user_query (str): The user query to be processed.
        route (str | None): The route determined by the router ("deep_research" or "normal").
        result (str | None): The final result from the selected processing branch.
        event_emitter (EventEmitter): The event emitter for streaming events during processing.
    """

    user_query: str
    route: str | None
    result: str | LMOutput | None
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
    lm_invoker=OpenAILMInvoker(
        model_name="gpt-5-nano",
        api_key=os.getenv("OPENAI_API_KEY"),
    ),
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

# Step 3: Configure Google Drive connector
# This connector enables the deep researcher to access and analyze documents from Google Drive
# To get the auth token, follow: https://platform.openai.com/docs/guides/tools-connectors-mcp?quickstart-panels=connector#authorizing-a-connector
# Required OAuth scopes: userinfo.email, userinfo.profile, drive.readonly
connector = NativeTool.mcp_connector(
    name="google_drive",
    connector_id="connector_googledrive",
    auth=os.getenv("GOOGLE_DRIVE_AUTH_TOKEN"),
)

# Step 4: Define the deep research branch
# This step processes complex queries requiring comprehensive research and analysis
# The Google Drive connector is passed as a tool, allowing the researcher to access Drive documents
deep_researcher = step(
    component=OpenAIDeepResearcher(
        model_name="o4-mini-deep-research",
        api_key=os.getenv("OPENAI_API_KEY"),
        tools=[
            connector
        ],  # Google Drive connector enables document access during research
    ),
    input_map={"query": "user_query", "event_emitter": "event_emitter"},
    output_state="result",
)

# Step 5: Define the normal response branch
# This step handles simple conversational queries using a standard response synthesizer
normal_response_synthesizer = step(
    component=ResponseSynthesizer.stuff_preset(
        # Note: Replace with your actual model ID (e.g., "openai/gpt-4o-mini")
        model_id="openai/gpt-5-nano",
        credentials=os.getenv("OPENAI_API_KEY"),
        user_template="{query}",
    ),
    input_map={"query": "user_query", "event_emitter": "event_emitter"},
    output_state="result",
)

# Step 6: Create the conditional switch step
# Routes to the appropriate branch based on the "route" field set by the router
conditional_step = switch(
    condition=lambda input: input["route"],
    branches={"deep_research": deep_researcher, "normal": normal_response_synthesizer},
)

# Step 7: Compose the pipeline
# The pipeline flows: router -> conditional_step (which routes to appropriate branch)
# Deep research queries will have access to Google Drive via the connector tool
deep_research_pipeline = router | conditional_step
deep_research_pipeline.state_type = DeepResearchState


async def main() -> None:
    """Run the deep research pipeline example with Google Drive integration.

    This function demonstrates how to use the pipeline with a sample query.
    The query "research information from my Google Drive about AI trends" will be classified as a
    deep research query and routed to the OpenAIDeepResearcher component, which
    has access to Google Drive for retrieving and analyzing documents.

    To test the normal query path, change the user_query to something like "hello"
    or "how are you".
    """
    event_emitter = EventEmitter.with_print_handler()
    state = DeepResearchState(
        user_query="research information from my Google Drive about AI trends",
        event_emitter=event_emitter,
        route=None,
        result=None,
    )

    result = await deep_research_pipeline.invoke(state)

    print(result)


if __name__ == "__main__":
    # Run the pipeline example
    # Prerequisites:
    #   1. Set OPENAI_API_KEY environment variable
    #   2. Set GOOGLE_DRIVE_AUTH_TOKEN environment variable
    #      Get the token from: https://platform.openai.com/docs/guides/tools-connectors-mcp?quickstart-panels=connector#authorizing-a-connector
    #      Required OAuth scopes: userinfo.email, userinfo.profile, drive.readonly
    asyncio.run(main())
