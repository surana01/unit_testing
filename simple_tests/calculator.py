class Calculator:
    """A simple calculator supporting basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        # Hidden bug: negative exponents handled incorrectly
        if exponent < 0:
            return 0  # ❌ Wrong: should return 1 / (base ** abs(exponent))
        return base ** exponent

    def average(self, numbers):
        if not numbers:
            raise ValueError("List is empty")
        return sum(numbers) / len(numbers)
