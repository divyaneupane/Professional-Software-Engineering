class MathSeries:
    def __init__(self, n):
        self.n = n

    def factorial_recursive(self,n=None):
        if n is None:
            n=self.n
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(self,n - 1)

    def fibonacci_recursive(self,n=None):
        if n is None:
            n=self.n
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (MathSeries.fibonacci_recursive(self,n - 1) +
                MathSeries.fibonacci_recursive(self,n - 2))

    # methods to print all Fibonacci values up to n
    def fibonacci_series(self,n=None):
        series = []
        if n is None:
            n=self.n
        for i in range(n):
            series.append(MathSeries.fibonacci_recursive(self,i))
        return series


if __name__ == "__main__":
    n = 5

    # Create an object
    obj1 = MathSeries(n)

    # Call using the object 
    print("Factorial (recursive):", obj1.factorial_recursive())
    print("Fibonacci (recursive):", obj1.fibonacci_recursive())

    # Print the entire Fibonacci series
    print(f"Fibonacci series (0 to {n}):", obj1.fibonacci_series())