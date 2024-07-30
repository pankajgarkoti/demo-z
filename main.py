from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
from constants import PIZZA_MENU
from uuid import uuid4

app = FastAPI()

PIZZA_MENU_MAP_ID = {item["id"]: item for item in PIZZA_MENU}


class GetMenu(BaseModel):
    id: int
    name: str
    price: float
    size: Literal["Regular", "Medium", "Large"] = "Medium"
    toppings: list[str] | None = (
        None  # None should mean the standard toppings that go with that pizza
    )


class OrderItem(BaseModel):
    id: int
    quantity: int = 1


@app.get("/menu")
def get_menu(name: str):
    """
    Get a menu item based on its name.
    """
    items = list(filter(lambda x: x["name"] == name, PIZZA_MENU))

    if len(items) == 0:
        raise HTTPException(404, "Menu item not found.")

    return items[0]


@app.post("/order")
def post_order(order_items: list[OrderItem]):
    """
    Get the total prize of an order.
    """
    total = 0
    for item in order_items:
        pizza = PIZZA_MENU_MAP_ID[item.id]
        total += pizza["price"] * item.quantity

    return {"order_id": uuid4().hex, "price": total}


if __name__ == "__main__":
    pass
