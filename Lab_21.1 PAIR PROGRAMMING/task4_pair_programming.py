"""Task 4: Pair Programming Simulation (Student A base + Student B AI enhancements)."""


# Student A: Initial inventory dictionary
def add_item(inv: dict, name: str, qty: int, price: float) -> None:
    inv[name] = {"qty": qty, "price": price}


# Student B (with AI assistance): Low-stock alert and total valuation
def inventory_report(inv: dict, low_threshold: int = 5) -> tuple[float, list[str]]:
    total_val = sum(v["qty"] * v["price"] for v in inv.values())
    low_stock = [k for k, v in inv.items() if v["qty"] < low_threshold]
    return round(total_val, 2), low_stock


if __name__ == "__main__":
    store = {}
    add_item(store, "Notebooks", 3, 50.0)
    add_item(store, "Pens", 20, 10.0)
    total, alerts = inventory_report(store)
    print(f"Total Inventory Value: Rs. {total}")
    print(f"Low Stock Alerts: {alerts}")
