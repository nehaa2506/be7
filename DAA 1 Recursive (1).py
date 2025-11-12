def fib(n):
    if n <= 1:
        return n  # Base case
    return fib(n-1) + fib(n-2)  # Recursive case

n = int(input("Enter number of terms: "))
print("Fibonacci sequence (Recursive):")

for i in range(n):
    print(fib(i), end=" ")
