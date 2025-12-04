
# Week 2 - Activity 4.2
# Description: Using a class with objects to calculate factorial and Fibonacci series
# and print the entire Fibonacci sequence

class MathSeries:
    # Recursive method to calculate factorial of a number
    def factorial_recursive(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")  # Handle negative input
        if n in (0, 1):
            return 1  # Base case: factorial of 0 or 1 is 1
        return n * self.factorial_recursive(n - 1)  # Recursive step

    # Recursive method to calculate nth Fibonacci number
    def fibonacci_recursive(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")  # Handle negative input
        if n == 0:
            return 0  # Base case: 0th Fibonacci is 0
        if n == 1:
            return 1  # Base case: 1st Fibonacci is 1
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)  # Recursive step

    # Method to generate the entire Fibonacci series up to n terms
    def fibonacci_sequence(self, n):
        sequence = []
        for i in range(n):
            sequence.append(self.fibonacci_recursive(i))  # Append each Fibonacci number to the list
        return sequence


if __name__ == "__main__":
    n = 7 # Example input number

    obj = MathSeries()  # Create an object of MathSeries class

    # Call factorial method using object
    print("Factorial (recursive):", obj.factorial_recursive(n))

    # Call nth Fibonacci method using object
    print("Fibonacci (recursive) for position", n, ":", obj.fibonacci_recursive(n))

    # Call Fibonacci sequence method using object to print entire series
    print("Fibonacci sequence up to position", n, ":", obj.fibonacci_sequence(n))
