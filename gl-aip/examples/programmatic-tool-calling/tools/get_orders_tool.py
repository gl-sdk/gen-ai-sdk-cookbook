"""Mock get_orders tool."""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

ORDERS_BY_USER_ID = {
    42: [
        {"order_id": "ORD-105", "item": "Wireless Mouse", "date": "2026-02-27", "status": "shipped"},
        {"order_id": "ORD-094", "item": "USB-C Hub", "date": "2026-02-20", "status": "delivered"},
        {"order_id": "ORD-088", "item": "Laptop Stand", "date": "2026-02-14", "status": "processing"},
    ],
    7: [{"order_id": "ORD-090", "item": "Noise-Canceling Headphones", "date": "2026-02-18", "status": "delivered"}],
}


class GetOrdersInput(BaseModel):
    """Input schema for get_orders."""

    user_id: int = Field(description="Internal customer ID returned by get_user")


class GetOrdersTool(BaseTool):
    """Return recent orders by user_id."""

    name: str = "get_orders"
    description: str = "Get recent orders by user_id and return order_id, item, date, status"
    args_schema: type[BaseModel] = GetOrdersInput

    def _run(self, user_id: int) -> dict[str, Any]:
        orders = ORDERS_BY_USER_ID.get(user_id, [])
        recent_orders = sorted(orders, key=lambda order: order["date"], reverse=True)
        if not recent_orders:
            return {
                "status": "not_found",
                "message": f"No orders found for user_id {user_id}.",
                "data": [],
            }
        return {
            "status": "ok",
            "message": f"Found {len(recent_orders)} recent orders for user_id {user_id}.",
            "data": recent_orders,
        }
