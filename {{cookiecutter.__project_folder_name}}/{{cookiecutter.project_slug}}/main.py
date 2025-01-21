"""The main module for the application."""

DIVIDE_BY_ZERO = "Cannot divide by zero"


class Greeter:
    """A simple class to greet the world or a specific person."""

    def greet(self, name: str | None = None) -> str:
        """Return a greeting message."""
        if name:
            return f"Hello, {name}!"
        return "Hello, World!"


class MathOperations:
    """A simple class for basic math operations."""

    @staticmethod
    def add(a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        """Subtract one number from another."""
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> float:
        """Divide one number by another."""
        if b == 0:
            raise ValueError(DIVIDE_BY_ZERO)
        return a / b


def main():
    greeter = Greeter()
    print(greeter.greet())
    print(greeter.greet("Alice"))
    math = MathOperations()
    print(math.add(5, 3))
    print(math.subtract(10, 4))
    print(math.multiply(6, 7))
    print(math.divide(8, 2))


if __name__ == "__main__":
    main()
