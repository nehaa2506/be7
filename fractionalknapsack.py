import java.util.Scanner;

public class EasyFractionalKnapsack {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Step 1: Input
        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        int[] profit = new int[n];
        int[] weight = new int[n];
        double[] ratio = new double[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter profit of item " + (i + 1) + ": ");
            profit[i] = sc.nextInt();
            System.out.print("Enter weight of item " + (i + 1) + ": ");
            weight[i] = sc.nextInt();
            ratio[i] = (double) profit[i] / weight[i]; // double ratio
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        // Step 2: Sort items by ratio (descending order)
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (ratio[i] < ratio[j]) {
                    double tempR = ratio[i];
                    ratio[i] = ratio[j];
                    ratio[j] = tempR;

                    int tempP = profit[i];
                    profit[i] = profit[j];
                    profit[j] = tempP;

                    int tempW = weight[i];
                    weight[i] = weight[j];
                    weight[j] = tempW;
                }
            }
        }

        // Step 3: Pick items (Fractional Knapsack logic)
        double totalProfit = 0.0;

        for (int i = 0; i < n; i++) {
            if (capacity == 0) break;

            if (weight[i] <= capacity) {
                totalProfit += profit[i];   // take full item
                capacity -= weight[i];
            } else {
                totalProfit += ratio[i] * capacity;  // take fraction
                capacity = 0;
            }
        }

        // Step 4: Output
        System.out.println("\nMaximum Profit = " + totalProfit);
        sc.close();
    }
}
