package acm;

import java.util.Scanner;

/**
 * Created by xiongchi on 2017/12/12.
 * 为了得到一个数的"相反数",我们将这个数的数字顺序颠倒,然后再加上原先的数得到"相反数"。例如,为了得到1325的"相反数",首先我们将该数的数字顺序颠倒,我们得到5231,之后再加上原先的数,我们得到5231+1325=6556.如果颠倒之后的数字有前缀零,前缀零将会被忽略。例如n = 100, 颠倒之后是1.
 输入描述:
 输入包括一个整数n,(1 ≤ n ≤ 10^5)

 输出描述:
 输出一个整数,表示n的相反数
 */
public class test3 {

    public static int run(int num){
        return num + reverseNum(num);
    }

    private static int reverseNum(int num){
        StringBuilder strNum = new StringBuilder();
        for(int i = num; ;i = i / 10){
            if(i / 10 == 0){
                strNum.append(i % 10);
                return Integer.parseInt(strNum.toString());
            }else{
                strNum.append(i % 10);
            }

        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = Integer.parseInt(sc.next());
        System.out.println(run(i));
    }
}
