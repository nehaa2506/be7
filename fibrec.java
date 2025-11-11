import java.util.*;

public class FibonacciRecursive {
    
    // Recursive function to find nth Fibonacci term
    static int fibonacci(int n) {
        if (n <= 1) 
            return n;    // Base case: F(0)=0, F(1)=1
        return fibonacci(n - 1) + fibonacci(n - 2); // Recursive call
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of terms: ");
        int n = sc.nextInt();

        System.out.println("Fibonacci Series:");
        for (int i = 0; i < n; i++) {
            System.out.print(fibonacci(i) + " ");
        }

        sc.close();
    }
}
