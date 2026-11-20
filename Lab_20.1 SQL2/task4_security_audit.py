"""Task 4: Security Audit — Insecure vs Secure Password & Secret Handling."""
import hashlib
import hmac
import os
import secrets

# --- INSECURE VERSION (Audited & Flagged) ---
# 1. Hardcoded secret key in source code
# 2. Weak MD5 hashing without salt
# 3. Non-constant-time == comparison (timing attack risk)

# --- SECURE REFACTORED VERSION ---
SECRET_KEY = os.environ.get("APP_SECRET_KEY", secrets.token_hex(16))


def hash_password_secure(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    """Hash password using PBKDF2-HMAC-SHA256 with a random 16-byte salt."""
    salt = salt or os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return salt, dk


def verify_password_secure(password: str, salt: bytes, expected_dk: bytes) -> bool:
    """Verify password in constant time to prevent timing side-channel attacks."""
    _, dk = hash_password_secure(password, salt)
    return hmac.compare_digest(dk, expected_dk)


if __name__ == "__main__":
    salt, stored = hash_password_secure("Ansika@2026")
    print("PBKDF2 Salt (hex):", salt.hex()[:16] + "...")
    print("Valid password check:  ", verify_password_secure("Ansika@2026", salt, stored))
    print("Invalid password check:", verify_password_secure("WrongPass", salt, stored))
