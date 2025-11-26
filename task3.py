n=int(input("Enter the number:"))
Fib=[1,1]
for i in range (n-2):
    sequence = Fib[i] + Fib[i+1]   #sum for next 
    Fib.append(sequence)
    


print(Fib[:n])



