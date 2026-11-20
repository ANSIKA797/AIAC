"""Task 1: Secure Login Script with regex input validation."""
import hashlib
import re

USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
PASSWORD_RE = re.compile(r"^(?=.*[A-Z])(?=.*\d).{8,}$")
USERS = {"ansika_23": hashlib.sha256(b"SecurePass1").hexdigest()}


def login(username: str, password: str) -> str:
    """Validate username and password format before checking credentials."""
    if not USERNAME_RE.match(username):
        return "Rejected: Invalid username format"
    if not PASSWORD_RE.match(password):
        return "Rejected: Weak password format"
    digest = hashlib.sha256(password.encode()).hexdigest()
    return "Login successful" if USERS.get(username) == digest else "Rejected: Invalid credentials"


if __name__ == "__main__":
    print("Test 1 (bad user):", login("admin'; --", "SecurePass1"))
    print("Test 2 (weak pwd):", login("ansika_23", "1234"))
    print("Test 3 (valid):   ", login("ansika_23", "SecurePass1"))
