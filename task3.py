n=int(input("Enter the number:"))
Fib=[1,1]
for i in range (n-2):
    sequence = Fib[i] + Fib[i+1]   #sum for next 
    Fib.append(sequence)
    


print(Fib[:n])




#part two using math library 
import math

n = int(input("Enter the number: "))
Fib = []

for i in range(n):
    fib_num = int(((1 + math.sqrt(5))**i - (1 - math.sqrt(5))**i) / (2**i * math.sqrt(5)))
    Fib.append(fib_num)

print(Fib)


