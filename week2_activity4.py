class Operations:
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * Operations.factorial(n-1)
   
    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return Operations.fibonacci(n-1) + Operations.fibonacci(n-2)
        

# print(Operations.factorial())
# print(Operations.fibonacci())

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = int(input("Enter a number to calculate factorial: "))
        print(f"Factorial of {num} is {Operations.factorial(num)}")
    elif choice == 2:
        num = int(input("Enter the position of the Fibonacci number: "))
        print(f"Fibonacci number at position {num} is {Operations.fibonacci(num)}")
    else:
        print("Invalid choice")


