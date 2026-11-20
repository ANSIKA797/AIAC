"""Task 4 (Python): Filter active users and format summary."""
users = [
    {"name": "Ansika", "active": True, "score": 95},
    {"name": "Vikram", "active": False, "score": 70},
    {"name": "Neha", "active": True, "score": 88},
]
top_active = [f"{u['name']}: {u['score']}" for u in users if u["active"]]
print("Active:", top_active)
