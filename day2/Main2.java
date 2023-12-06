package day2;


import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in).useDelimiter("\n");
        int res = 0;
        int cnt = 1;
        while (sc.hasNextLine()) {
            String[] s = sc.nextLine().substring(7).split(";");
            int valid = 1;
            int large = 1000000;
            int[] cmin = {0, 0, 0};
            for (String round : s) {
                for (String a : round.split(",")) {
                    int num = Integer.parseInt(a.replaceAll("[^0-9]", ""));
                    if (a.contains("red")) {
                        cmin[0] = Integer.max(cmin[0], num);
                    }
                    if (a.contains("green")) {
                        cmin[1] = Integer.max(cmin[1], num);
                    }
                    if (a.contains("blue")) {
                        cmin[2] = Integer.max(cmin[2], num);
                    }
                }
            }
            res += cmin[0]*cmin[1]*cmin[2];
        }
        System.out.println(res);
    }
}