import requests
from pprint import pprint

BASE_URL = "http://127.0.0.1:8000"


def test_menu():
    res = requests.get(
        f"{BASE_URL}/menu",
        params={
            "name": "Pepperoni",
        },
    )
    print("=============")
    pprint(res.json())
    print("=============")


def test_orders():
    res = requests.post(
        f"{BASE_URL}/order",
        json=[
            {"id": 1, "quantity": 2},
            {"id": 3, "quantity": 5},
        ],
    )
    print("=============")
    pprint(res.json())
    print("=============")


if __name__ == "__main__":
    test_menu()
    test_orders()
