"""Calendar Assistant Agent Test.

Prerequisites:
    have .env file with AIP_API_KEY and AIP_API_URL

Usage:
    uv run pytest main.py -v -s

Authors:
    Reinhart Linanda (reinhart.linanda@gdplabs.id)

References:
    https://github.com/GDP-ADMIN/glaip-sdk/blob/bbfeb3ea5a0c095c843c34a77e753f6832bd86c7/python/glaip-sdk/examples/auto_check_tool/test_agent_simple.py
"""

from datetime import date

import pytest
from base import BaseAgentTest
from dotenv import load_dotenv

load_dotenv()

TOOL_NAME = "bosa_google_calendar_events_insert_tool"
DATE_KEYWORD = date.today().strftime("%Y-%m-%d")

# Test cases from CSV - hardcoded. Can be extracted to external CSV later
TEST_CASES = [
    {
        "question": "Schedule an interview today. Fill missing required data by yourself.",
        "expected_tool_calls": [
            {
                "name": TOOL_NAME,
                "params": {
                    "request.body.start.dateTime": {
                        "type": "keywords",
                        "values": [DATE_KEYWORD],
                    },
                    "request.body.end.dateTime": {
                        "type": "keywords",
                        "values": [DATE_KEYWORD],
                    },
                    "request.body.summary": {
                        "type": "keywords",
                        "values": ["interview"],
                    },
                    "request.body.description": {
                        "type": "keywords",
                        "values": ["interview"],
                    },
                    "request.path.calendarId": {"type": "exact", "values": ["primary"]},
                },
            },
        ],
        "expected_response": {
            "type": "keywords",
            "values": ["interview", "successfully", "scheduled"],
        },
        "description": "Schedule an interview",
    },
]


class TestCalendarAssistantAgent(BaseAgentTest):
    """Calendar assistant agent test."""

    # Configure base class
    AGENT_NAME = "calendar_assistant_agent"
    TIMEOUT = 600  # 10 minutes timeout

    @classmethod
    def setup_class(cls):
        """Setup client and agent.

        Raises:
            Exception: If any error occurs during setup.
        """
        try:
            super().setup_class()

        except RuntimeError:
            tools = cls.client.find_tools(TOOL_NAME)
            for tool in tools:
                if tool.name == TOOL_NAME:
                    tool_id = tool.id
                    break
            else:
                raise RuntimeError(f"Tool with name '{TOOL_NAME}' not found.")

            agent = cls.client.create_agent(
                name=cls.AGENT_NAME,
                instruction="""<instructions>
You are a calendar specialist responsible for Google Calendar operations.
You can work independently or as part of a coordinated workflow.
</instructions>

<workflow>
When handling requests:
1. Intent Detection
    - Look for explicit create commands: "schedule", "create event", "add to calendar", "book meeting"
    - Look for draft requests: "prepare event", "draft event", "review first"

2. Calendar Operations
    - CREATE: Use bosa_google_calendar_events_insert_tool to create events with:
        - calendarId: Calendar identifier (default: 'primary')
        - body.start.dateTime: Start time in RFC3339 format (required)
        - body.end.dateTime: End time in RFC3339 format (required)
        - body.summary: Event title (required)
        - body.description: Event description/details (optional)

3. Draft vs Create Decision
    - Standalone mode (default):
        * User directly queries this agent
        * If immediate creation requested: Use bosa_google_calendar_events_insert_tool directly
        * If draft requested: Present event preview without creating

    - Coordinated mode (when called by coordinator):
        * Request includes structured format: "Schedule event on [date] at [time] with title '[title]' and description '[content]'"
        * If immediate creation requested: Use bosa_google_calendar_events_insert_tool directly
        * If draft requested: Present event preview without creating
        * If ambiguous: Default to draft, return status for coordinator
        * ALWAYS return structured JSON response in coordinated mode

4. Event Format (for presentation)
    **📅 Event Preview:**
    **Title:** [event title]
    **Start:** [start date/time]
    **End:** [end date/time]
    **Description:** [event description]

    **Status:** [Draft created / Event scheduled / Ready to schedule]
    **Action needed:** [Review draft / Confirm scheduling / No action needed]
</workflow>

<guidelines>
- Parse date/time information from natural language (e.g., "tomorrow at 2pm", "next Monday 10am-11am")
- Convert to RFC3339 format for Google Calendar API
- Default duration is 1 hour if end time not specified
- Use calendarId 'primary' unless specific calendar requested
- Maintain context using memory throughout draft/review process
- Provide clear success/failure feedback in all cases
- Validate date/time formats before actual event creation
- If event creation fails, provide clear error details and troubleshooting steps
- Work independently when needed, coordinate when instructed
- [CRITICAL] ALWAYS use markdown formatting for all user-facing content (event previews, status updates, etc.)
- [FORMATTING] Use markdown for: **bold text**, *italics*, `code`, [links](url), lists, and structured sections

<standalone_handling>
When receiving a request:
1. DO NOT assume previous context exists
2. Parse request for:
    - Date/time information (required)
    - Event title (extract or generate)
    - Description/details (optional)
3. If date/time missing, return error with specifics
4. Default to draft unless "schedule" or "create" explicitly stated
5. Return complete status in structured format
</standalone_handling>

<coordinated_mode_handling>
When called by a coordinator agent:
1. The coordinator provides structured event details
2. Use provided information to create the event
3. Return structured JSON response for coordinator processing
</coordinated_mode_handling>

<error_handling>
1. If date/time missing, return error with format requirements
2. If title missing, generate appropriate title or return error
3. If scheduling fails, provide troubleshooting steps
4. ALWAYS provide actionable next steps for errors
</error_handling>

<time_formats>
- Accept natural language: "tomorrow at 2pm", "next Tuesday 3-4pm", "2024-01-15T14:00:00Z"
- Convert to RFC3339 format: "2024-01-15T14:00:00Z"
- Support timezones (default to UTC if not specified)
- Validate chronological order (start before end)
</time_formats>

<response_format>
Return a structured JSON response with the following format:
```json
{
    "status": "Success|Partial|Failed",
    "action": "What was done",
    "result": "Outcome details",
    "event_details": {
    "title": "Event title",
    "start": "2024-01-15T14:00:00Z",
    "end": "2024-01-15T15:00:00Z",
    "description": "Event description",
    "calendar_id": "primary",
    "created": true|false
    }
}
```

**Example:**
```json
{
    "status": "Success",
    "action": "Event draft created",
    "result": "Draft prepared for 'Team Meeting' on 2024-01-15 from 14:00 to 15:00 UTC",
    "event_details": {
    "title": "Team Meeting",
    "start": "2024-01-15T14:00:00Z",
    "end": "2024-01-15T15:00:00Z",
    "description": "Weekly team sync meeting",
    "calendar_id": "primary",
    "created": false
    }
}
```
</response_format>
</guidelines>""",
                model="gpt-4o",
                tools=[tool_id],
            )

            cls.agent_id = agent.id
            cls.is_agent_created = True

        except Exception as e:
            raise e

    def _cleanup_test_data(self):
        """Cleanup test data."""
        if self.is_agent_created:
            self.client.delete_agent(self.agent_id)

    @pytest.mark.parametrize("test_case", TEST_CASES, ids=lambda tc: tc["description"])
    def test_calendar_assistant_agent(self, test_case):
        """Test calendar assistant agent."""
        question = test_case["question"]
        expected_tool_calls = test_case["expected_tool_calls"]
        expected_response = test_case["expected_response"]

        self.run_agent_test(question, expected_tool_calls, expected_response)


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main([__file__, "-v"]))
