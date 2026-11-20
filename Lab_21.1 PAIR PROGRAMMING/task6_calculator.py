"""Task 6: Feature Expansion — Calculator with Validation and History."""


class Calculator:
    def __init__(self):
        self.history: list[str] = []

    def calculate(self, a: float, op: str, b: float) -> float:
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            res = a / b
        else:
            raise ValueError(f"Unsupported operator: {op}")
        self.history.append(f"{a} {op} {b} = {res}")
        return res


if __name__ == "__main__":
    calc = Calculator()
    print("12 + 8 =", calc.calculate(12, "+", 8))
    print("15 / 3 =", calc.calculate(15, "/", 3))
    print("History:", calc.history)
