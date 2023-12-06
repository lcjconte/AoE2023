package day2;


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in).useDelimiter("\n");
        int res = 0;
        int cnt = 1;
        while (sc.hasNextLine()) {
            String[] s = sc.nextLine().substring(7).split(";");
            int valid = 1;
            for (String round : s) {
                for (String a : round.split(",")) {
                    int num = Integer.parseInt(a.replaceAll("[^0-9]", ""));
                    if (a.contains("red")) {
                        valid &= num <= 12 ? 1 : 0;
                    }
                    if (a.contains("green")) {
                        valid &= num <= 13 ? 1 : 0;
                    }
                    if (a.contains("blue")) {
                        valid &= num <= 14 ? 1 : 0;
                    }
                    if (valid < 1) {break;}
                }
                if (valid<1) {break;}
            }
            res += cnt * valid;
            cnt++;
        }
        System.out.println(res);
    }
}