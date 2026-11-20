"""Task 2: SQL Injection Prevention using parameterized SQLite queries."""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, role TEXT)")
conn.executemany("INSERT INTO users VALUES (?, ?, ?)", [
    (1, "ansika", "student"),
    (2, "admin", "administrator"),
])

# Vulnerable approach (DO NOT USE): f"SELECT * FROM users WHERE username = '{user_input}'"
def fetch_user_secure(username: str):
    """Fetch user safely using a parameterized prepared statement."""
    cur = conn.execute("SELECT id, username, role FROM users WHERE username = ?", (username,))
    return cur.fetchall()


if __name__ == "__main__":
    print("Normal lookup ('ansika'):     ", fetch_user_secure("ansika"))
    print("SQLi attempt (OR 1=1):     ", fetch_user_secure("' OR '1'='1"))
