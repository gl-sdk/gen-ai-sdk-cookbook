"""Mock get_user tool."""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

USERS = {
    "alice": {
        "id": 42,
        "name": "Alice",
        "email": "alice@email.com",
        "phone": "+1-555-0101",
    },
    "bob": {
        "id": 7,
        "name": "Bob",
        "email": "bob@email.com",
        "phone": "+1-555-0107",
    },
}


class GetUserInput(BaseModel):
    """Input schema for get_user."""

    name: str = Field(description="Full name of the customer, for example Alice")


class GetUserTool(BaseTool):
    """Return a user record by name."""

    name: str = "get_user"
    description: str = "Get a customer profile by name and return id, name, email, phone"
    args_schema: type[BaseModel] = GetUserInput

    def _run(self, name: str) -> dict[str, Any]:
        user = USERS.get(name.strip().lower())
        if not user:
            return {
                "status": "not_found",
                "message": f"No user found for name '{name}'.",
                "data": None,
            }
        return {
            "status": "ok",
            "message": f"User '{user['name']}' found.",
            "data": user,
        }
