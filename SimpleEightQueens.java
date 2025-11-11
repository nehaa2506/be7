import java.util.*;
public class SimpleEightQueens {
    static int N = 8;
    static int[] board = new int[N];

    static boolean isSafe(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || Math.abs(board[i] - col) == Math.abs(i - row))
                return false;
        }
        return true;
    }

    static boolean solve(int row) {
        if (row == N) return true;
        for (int col = 0; col < N; col++) {
            if (isSafe(row, col)) {
                board[row] = col;
                if (solve(row + 1)) return true;
            }
        }
        return false;
    }

    static void printBoard() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                System.out.print(board[i] == j ? "Q " : ". ");
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int firstCol = 0;
        board[0] = firstCol;
        if (solve(1))
            printBoard();
        else
            System.out.println("No solution found.");
    }
}
