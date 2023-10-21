#Java Base
import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int[][] temp = new int[6][2]; //6*2
        int[] temp_height = new int[3];
        int[] temp_width = new int[3];
        int mid_width = 0, mid_height = 0;
        int width = 0, height = 0;
        if (num1 < 1 || num1 > 20) {
            return;
        }
        for (int i = 0; i < 6; i++) {
            int dir = scanner.nextInt();
            int number = scanner.nextInt();
            if (dir == 1) {
                temp[i][0] = dir;
                temp[i][1] = number;
                temp_width[width] = number;
                width++;
            } else if (dir == 2) {
                temp[i][0] = dir;
                temp[i][1] = number;
                temp_width[width] = number;
                width++;
            } else if (dir == 3) {
                temp[i][0] = dir;
                temp[i][1] = number;
                temp_height[height] = number;
                height++;
            } else if (dir == 4) {
                temp[i][0] = dir;
                temp[i][1] = number;
                temp_height[height] = number;
                height++;
            }

        }
        int max_height = temp_height[0], max_width = temp_width[0];
        for (int i = 1; i < 3; i++) {
            if(temp_height[i] > max_height)max_height = temp_height[i];
        }
        for (int i = 1; i < 3; i++) {
            if(temp_width[i] > max_width)max_width = temp_width[i];
        }
        int j;
        for (int i = 0; i < 6; i++) {
            if (i == 0) {
                j = temp[1][0];
                if (j == 1 || j == 2) {
                    if (j == temp[5][0]) {
                        mid_height = temp[i][1];
                    }
                }
                if (j == 3 || j == 4) {
                    if (j == temp[5][0]) {
                        mid_width = temp[i][1];
                    }
                }
            } else if (i == 5) {
                j = temp[0][0];
                if (j == 1 || j == 2) {
                    if (j == temp[4][0]) {
                        mid_height = temp[i][1];
                    }
                }
                if (j == 3 || j == 4) {
                    if (j == temp[4][0]) {
                        mid_width = temp[i][1];
                    }
                }
            } else {
                j = temp[i + 1][0];
                if (j == 1 || j == 2) {
                    if (j == temp[i - 1][0]) mid_height = temp[i][1];
                }
                if (j == 3 || j == 4) {
                    if (j == temp[i - 1][0]) mid_width = temp[i][1];
                }

            }
        }
        int not_squre = mid_width * mid_height;
        int really_squre = max_height * max_width;
        int sum = (really_squre - not_squre) * num1;
        System.out.println(sum);
        scanner.close();
    }
}