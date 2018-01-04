package acm;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by xiongchi on 2017/12/28.
 * 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
 */
public class Test15 {

    public int NumberOf1(int n) {
       int count = 0;
       while(n !=0){
           if((n & 1) == 1){
               count++;
           }
           n = n >>> 1;   //逻辑右移  n >> 1 算术右移 负数最高位补1 出现死循环
       }
       return count;
    }


    public int NumberOf2(int n) {
      int count = 0;
      while(n != 0){
          n = (n - 1)&n;
          ++count;
      }
      return count;
    }


    public int NumberOf3(int n) {
        return Integer.toBinaryString(n).replaceAll("0", "").length();
    }

    public int NumberOf4(int n) {
        return Integer.bitCount(n);
    }

    public static void main(String[] args) {
        Test15 t15 = new Test15();
        System.out.println(t15.NumberOf1(-3));
        System.out.println(t15.NumberOf2(-3));
        System.out.println(t15.NumberOf3(-3));
        System.out.println(t15.NumberOf4(-9822));
    }


}
