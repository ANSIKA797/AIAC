"""Online Food Ordering RESTful API with FastAPI."""
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title="Online Food Ordering API")

MENU = {
    1: {"id": 1, "name": "Margherita Pizza", "price": 299},
    2: {"id": 2, "name": "Veg Biryani", "price": 240},
    3: {"id": 3, "name": "Cold Coffee", "price": 120},
}
orders_db: dict[int, dict] = {}
next_order_id = 1


class OrderRequest(BaseModel):
    customer_name: str
    item_ids: list[int]


@app.get("/menu")
def get_menu():
    """List available dishes. (Improvement: add limit/offset pagination for large menus.)"""
    return {"menu": list(MENU.values())}


@app.post("/order", status_code=201)
def place_order(order: OrderRequest):
    """Place a new food order. (Improvement: protect with JWT user authentication.)"""
    global next_order_id
    if not order.item_ids or any(i not in MENU for i in order.item_ids):
        raise HTTPException(status_code=400, detail="Invalid or empty menu item IDs")
    total = sum(MENU[i]["price"] for i in order.item_ids)
    record = {
        "order_id": next_order_id,
        "customer_name": order.customer_name,
        "items": [MENU[i]["name"] for i in order.item_ids],
        "total": total,
        "status": "Preparing",
    }
    orders_db[next_order_id] = record
    next_order_id += 1
    return record


@app.get("/order/{order_id}")
def track_order(order_id: int):
    """Track current order status."""
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]


@app.put("/order/{order_id}")
def update_order(order_id: int, order: OrderRequest):
    """Update items in an existing order."""
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    if not order.item_ids or any(i not in MENU for i in order.item_ids):
        raise HTTPException(status_code=400, detail="Invalid menu item IDs")
    orders_db[order_id]["items"] = [MENU[i]["name"] for i in order.item_ids]
    orders_db[order_id]["total"] = sum(MENU[i]["price"] for i in order.item_ids)
    return orders_db[order_id]


@app.delete("/order/{order_id}")
def cancel_order(order_id: int):
    """Cancel an existing order."""
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"cancelled": orders_db.pop(order_id)}


if __name__ == "__main__":
    client = TestClient(app)
    r1 = client.get("/menu")
    assert r1.status_code == 200 and len(r1.json()["menu"]) == 3
    r2 = client.post("/order", json={"customer_name": "Ansika", "item_ids": [1, 3]})
    assert r2.status_code == 201 and r2.json()["total"] == 419
    r3 = client.put("/order/1", json={"customer_name": "Ansika", "item_ids": [2]})
    assert r3.status_code == 200 and r3.json()["total"] == 240
    r4 = client.delete("/order/1")
    assert r4.status_code == 200
    print("GET  /menu ->", len(r1.json()["menu"]), "dishes")
    print("POST /order ->", r2.json())
    print("PUT  /order/1 ->", r3.json())
    print("DELETE /order/1 ->", r4.json())
    print("All 4 assert test cases PASSED.")
