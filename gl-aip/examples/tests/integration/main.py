"""Calendar Assistant Agent Test.

Prerequisites:
    have .env file with AIP_API_KEY and AIP_API_URL set to the staging environment

Usage:
    uv run pytest main.py -v
    or
    uv run pytest main.py -v -s (for debug)

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

DATE_KEYWORD = date.today().strftime("%Y-%m-%d")

# Test cases from CSV - hardcoded. Can be extracted to external CSV later
TEST_CASES = [
    {
        "question": "Schedule an interview today. Fill missing required data by yourself.",
        "expected_tool_calls": [
            {
                "name": "bosa_google_calendar_events_insert_tool",
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
