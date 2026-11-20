"""Task 5: Replacing Insecure pickle.load() with Safe JSON Serialization."""
import json

# Why pickle is dangerous:
# pickle.load() can execute arbitrary Python code via __reduce__ during deserialization.
# Attackers can craft malicious pickle payloads to run OS commands on the server.

def save_user_safe(data: dict) -> str:
    """Serialize user profile safely to JSON."""
    return json.dumps(data, indent=2)


def load_user_safe(payload: str) -> dict:
    """Deserialize user profile safely from JSON (data-only, no code execution)."""
    obj = json.loads(payload)
    if not isinstance(obj, dict):
        raise ValueError("Expected JSON object")
    return obj


if __name__ == "__main__":
    user = {"name": "Adagiri Ansika", "batch": 23, "roles": ["student"]}
    serialized = save_user_safe(user)
    restored = load_user_safe(serialized)
    print("Serialized JSON:", serialized)
    print("Safely Restored:", restored)
