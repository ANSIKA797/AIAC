"""Task 2 (Translated): Pythonic recursive factorial function."""


def factorial(n: int) -> int:
    """Compute n! recursively for non-negative integers."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return 1 if n <= 1 else n * factorial(n - 1)


if __name__ == "__main__":
    for v in (0, 1, 5, 7):
        print(f"factorial({v}) = {factorial(v)}")
