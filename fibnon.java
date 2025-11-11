import java.util.*;

public class FibonacciNonRecursive {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of terms: ");
        int n = sc.nextInt();

        int a = 0, b = 1, c;

        System.out.println("Fibonacci Series:");

        if (n >= 1)
            System.out.print(a + " ");  // print first term
        if (n >= 2)
            System.out.print(b + " ");  // print second term

        for (int i = 3; i <= n; i++) {
            c = a + b;         // next term
            System.out.print(c + " ");
            a = b;             // move forward
            b = c;
        }

        sc.close();
    }
}
