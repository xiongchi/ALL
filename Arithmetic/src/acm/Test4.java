package acm;

import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.Scanner;



/**
 * Created by xiongchi on 2017/12/12.
 * "aaabbcc" 3+2+2/3
 */
public class Test4 {

    public static float run(String str){
        ArrayList<Integer> arr = new ArrayList<>();
        char flag = str.charAt(0);
        int numFlag = 1;
        for(int i = 1; i < str.length(); i++){
            if( i == str.length() - 1){
                if(flag == str.charAt(i)){
                    numFlag ++;
                    arr.add(numFlag);
                }else{
                    arr.add(1);
                }
            }
            if(flag == str.charAt(i)){
                numFlag ++;
            }else{
                arr.add(numFlag);
                flag = str.charAt(i);
                numFlag = 1;
            }
        }

        int sum = 0;
        for(int num : arr){
            sum += num;
        }
        float avg = (float)sum/ arr.size();
        return avg;
    }

    public static void main(String[] args) {

        NumberFormat nf = NumberFormat.getNumberInstance();
        nf.setMaximumFractionDigits(2);
        System.out.println(nf.format(1.131911));
        Scanner sc = new Scanner(System.in);
        System.out.println(new Formatter().format("%.2f", run(sc.next())).toString());
    }
}
