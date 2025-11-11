import java.util.*;

public class HuffmanC {

    static class Node {
        int f;            // frequency
        String ch;        // character
        Node l, r;        // left and right child

        Node(int f, String ch, Node l, Node r) {
            this.f = f;
            this.ch = ch;
            this.l = l;
            this.r = r;
        }
    }

    // Recursive function to print Huffman codes
    static void print(Node root, String code) {
        if (root == null) return;
        if (root.l == null && root.r == null) { // Leaf node (actual character)
            System.out.println(root.ch + " -> " + code);
            return;
        }
        print(root.l, code + "0"); // Left edge → 0
        print(root.r, code + "1"); // Right edge → 1
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("===== HUFFMAN CODING =====");
        System.out.print("Enter number of characters: ");
        int n = sc.nextInt();

        String[] c = new String[n];
        int[] f = new int[n];

        // Take character and frequency input
        System.out.println("\nEnter characters and their frequencies:");
        for (int i = 0; i < n; i++) {
            System.out.print("Character " + (i + 1) + ": ");
            c[i] = sc.next();
            System.out.print("Frequency of " + c[i] + ": ");
            f[i] = sc.nextInt();
        }

        // Create a priority queue (min-heap) sorted by frequency
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.f));
        for (int i = 0; i < n; i++) {
            pq.add(new Node(f[i], c[i], null, null));
        }

        // Build Huffman Tree
        while (pq.size() > 1) {
            Node a = pq.poll(); // smallest
            Node b = pq.poll(); // next smallest
            Node parent = new Node(a.f + b.f, "", a, b); // combined node
            pq.add(parent);
        }

        // Root of Huffman Tree
        Node root = pq.poll();

        // Print Huffman codes
        System.out.println("\nHuffman Codes:");
        print(root, "");

        sc.close();
    }
}
