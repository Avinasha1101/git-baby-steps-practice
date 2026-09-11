class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the result of a minus b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the result of a divided by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
