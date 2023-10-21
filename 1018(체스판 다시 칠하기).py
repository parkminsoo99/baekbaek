#JAVA Base
import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int number1 = scanner.nextInt();
        int number2 = scanner.nextInt();
        if(number1 < 8 || number2 < 8 || number1 > 50 || number2 > 50) return;
        char[][] chess = new char[number1][number2];
        int[] check_list = new int[(number1+1-8)*(number2+1-8)];
        int chainNodeX = 0, chainNodeY = 0;
        for (int i = 0; i < number1; i++) {
            String temp = scanner.next();
            for (int j = 0; j < number2; j++) {
                chess[i][j] = temp.charAt(j);
            }
        }
        int a=0;

        while (chainNodeY <= number1 - 8) {
            int check = 0;
            for (int i = chainNodeY; i < 8 + chainNodeY; i++) {
                for (int j = chainNodeX; j < 8 + chainNodeX; j++) {
                    if (chess[chainNodeY][chainNodeX] == 'B') {
                        if (i == chainNodeY || i == 2 + chainNodeY || i == 4 + chainNodeY || i == 6 + chainNodeY){
                            if (j == chainNodeX && chess[i][chainNodeX] != 'B') {
                                check++;}
                            else if (j == 1 + chainNodeX && chess[i][1+ chainNodeX] != 'W') {
                                check++;}
                            else if (j == 2 + chainNodeX && chess[i][2+ chainNodeX] != 'B') {
                                check++;}
                            else if (j == 3 + chainNodeX && chess[i][3+ chainNodeX] != 'W') {
                                check++;}
                            else if (j == 4 + chainNodeX && chess[i][4+ chainNodeX] != 'B') {
                                check++;}
                            else if (j == 5 + chainNodeX && chess[i][5+ chainNodeX] != 'W') {
                                check++;}
                            else if (j == 6 + chainNodeX && chess[i][6+ chainNodeX] != 'B') {
                                check++;}
                            else if (j == 7 + chainNodeX && chess[i][7+ chainNodeX] != 'W') {
                                check++;}
                        } else if (i == 1 + chainNodeY || i == 3 + chainNodeY || i == 5 + chainNodeY || i == 7 + chainNodeY) {
                            if (j == chainNodeX && chess[i][chainNodeX] != 'W') {
                            check++;}
                            else if (j == 1 + chainNodeX && chess[i][1+ chainNodeX] != 'B') {
                           check++;}
                            else if (j == 2 + chainNodeX && chess[i][2+ chainNodeX] != 'W') {
                            check++;}
                            else if (j == 3 + chainNodeX && chess[i][3+ chainNodeX] != 'B') {
                                check++;}
                            else if (j == 4 + chainNodeX && chess[i][4+ chainNodeX] != 'W') {
                                check++;}
                            else if (j == 5 + chainNodeX && chess[i][5+ chainNodeX] != 'B') {
                                check++;}
                            else if (j == 6 + chainNodeX && chess[i][6+ chainNodeX] != 'W') {
                             check++;}
                            else if (j == 7 + chainNodeX && chess[i][7+ chainNodeX] != 'B') {
                            check++;}
                        }
                    }
                    if (chess[chainNodeY][chainNodeX] == 'W') {
                        if (i == chainNodeY || i == 2 + chainNodeY || i == 4 + chainNodeY || i == 6 + chainNodeY) {
                            if (j == chainNodeX && chess[i][chainNodeX] != 'W') check++;
                            else if (j == 1 + chainNodeX && chess[i][1+ chainNodeX] != 'B') check++;
                            else if (j == 2 + chainNodeX && chess[i][2+ chainNodeX] != 'W') check++;
                            else if (j == 3 + chainNodeX && chess[i][3+ chainNodeX] != 'B') check++;
                            else if (j == 4 + chainNodeX && chess[i][4+ chainNodeX] != 'W') check++;
                            else if (j == 5 + chainNodeX && chess[i][5+ chainNodeX] != 'B') check++;
                            else if (j == 6 + chainNodeX && chess[i][6+ chainNodeX] != 'W') check++;
                            else if (j == 7 + chainNodeX && chess[i][7+ chainNodeX] != 'B') check++;
                        } else if (i == 1 + chainNodeY || i == 3 + chainNodeY || i == chainNodeY + 5 || i == chainNodeY + 7) {
                            if (j == chainNodeX && chess[i][chainNodeX] != 'B') check++;
                            else if (j == 1 + chainNodeX && chess[i][1+ chainNodeX] != 'W') check++;
                            else if (j == 2 + chainNodeX && chess[i][2+ chainNodeX] != 'B') check++;
                            else if (j == 3 + chainNodeX && chess[i][3+ chainNodeX]!= 'W') check++;
                            else if (j == 4 + chainNodeX && chess[i][4+ chainNodeX] != 'B') check++;
                            else if (j == 5 + chainNodeX && chess[i][5+ chainNodeX] != 'W') check++;
                            else if (j == 6 + chainNodeX && chess[i][6+ chainNodeX]!= 'B') check++;
                            else if (j == 7 + chainNodeX && chess[i][7+ chainNodeX] != 'W') check++;
                        }
                    }
                }
            }
            check_list[a] = Math.min(check,64-check);
            a++;
            chainNodeX++;
            if (chainNodeX > number2 - 8) {
                chainNodeY++;
                chainNodeX = 0;
            }
        }
            int temp = check_list[0];
            for (int i = 1; i < check_list.length; i++) {
                temp = Math.min(temp,check_list[i]);
            }
            System.out.println(temp);

        }
    }