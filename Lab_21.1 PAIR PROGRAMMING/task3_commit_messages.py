"""Task 3: AI-Style Conventional Commit Message Generator."""


def generate_commit_message(change_type: str, scope: str, diff_summary: str) -> str:
    """Generate a concise Conventional Commit message from a change summary."""
    return f"{change_type}({scope}): {diff_summary.strip().rstrip('.')}"


if __name__ == "__main__":
    human_msgs = ["updated code", "fixed bug in login"]
    ai_msgs = [
        generate_commit_message("feat", "todo", "add priority levels and index validation"),
        generate_commit_message("fix", "auth", "enforce regex validation on login username"),
    ]
    for h, a in zip(human_msgs, ai_msgs):
        print(f"Human: {h:22s} | AI: {a}")
