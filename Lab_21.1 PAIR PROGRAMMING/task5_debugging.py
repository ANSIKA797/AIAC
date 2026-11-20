"""Task 5: AI-Assisted Debugging — Buggy vs Corrected Average & Discount."""


# Buggy version:
# def apply_discount_buggy(price, pct): return price - pct  # Wrong: subtracted raw pct
# def avg_buggy(nums): return sum(nums) / len(nums)        # Crashes on empty list

def apply_discount(price: float, pct: float) -> float:
    """Correctly apply percentage discount with bounds check."""
    if not (0 <= pct <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return round(price * (1 - pct / 100), 2)


def safe_average(nums: list[float]) -> float:
    """Compute average safely, returning 0.0 for empty lists."""
    return round(sum(nums) / len(nums), 2) if nums else 0.0


if __name__ == "__main__":
    print("Discounted (1000, 15%):", apply_discount(1000, 15))
    print("Average ([80, 90, 95]):", safe_average([80, 90, 95]))
    print("Average ([]):          ", safe_average([]))
