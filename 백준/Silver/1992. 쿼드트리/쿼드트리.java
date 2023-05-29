import java.io.*;

public class Main {
    public static char[][] image;

    public static boolean check(int x, int y, int n) {
        for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                if (image[i][j] != image[x][y]) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void QuadTree(int x, int y, int n) {
        if (check(x, y, n)) {
            System.out.print(image[x][y]);
        } else {
            System.out.print('(');
            n /= 2;
            QuadTree(x, y, n);
            QuadTree(x, y + n, n);
            QuadTree(x + n, y, n);
            QuadTree(x + n, y + n, n);
            System.out.print(')');
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        image = new char[N][N];
        for (int i = 0; i < N; i++) {
            image[i] = br.readLine().toCharArray();
        }

        QuadTree(0, 0, N);
    }
}