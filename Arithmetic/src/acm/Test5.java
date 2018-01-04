package acm;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by xiongchi on 2017/12/15.
 */
public class Test5 {

    public static int run(Object[] num){
        Integer maxNum = Integer.MIN_VALUE;
        for(int i = 0; i < num.length; i++){
            num[i] = reverseNum((int)num[i]);
            if((int)num[i] > maxNum){
                maxNum = (int)num[i];
            }
        }
        return maxNum;
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
        String[] numStr = sc.next().split(",");
        ArrayList<Integer> arr = new ArrayList<>();
        for(int j= 0; j < numStr.length;j++){
            arr.add(Integer.parseInt(numStr[i]));
        }
        System.out.println(run(arr.toArray()));
    }
}