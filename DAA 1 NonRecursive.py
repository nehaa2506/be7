def fibonacci_iterative(n):
    
    a, b = 0, 1
    

    fibonacci_sequence = []
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        
        a, b = b, a + b
    
    return fibonacci_sequence


n = int(input("Enter the number of terms: "))


fib_sequence = fibonacci_iterative(n)


print(f"The first {n} Fibonacci numbers are: {fib_sequence}")
