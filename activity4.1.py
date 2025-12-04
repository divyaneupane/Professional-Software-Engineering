class MathSeries:
    @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)

    @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2)
    
    @staticmethod
    def fibonacci_sequence(n):
        """Return Fibonacci sequence up to n terms"""
        return [MathSeries.fibonacci_recursive(i) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    obj = MathSeries()

    print("Factorial (recursive):", obj.factorial_recursive(n))
    # print("Fibonacci (recursive) for position", n, ":", obj.fibonacci_recursive(n))
    
    # Print the entire Fibonacci sequence up to n
    print("Fibonacci sequence up to position", n, ":", obj.fibonacci_sequence(n))
