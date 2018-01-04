package acm;

import java.util.ArrayList;

/**
 * Created by xiongchi on 2017/12/11.
 * 描述
 现在，有一行括号序列，请你检查这行括号是否配对。
 输入
 第一行输入一个数N（0<N<=100）,表示有N组测试数据。后面的N行输入多组输入数据，每组输入数据都是一个字符串S(S的长度小于10000，且S不是空串），测试数据组数少于5组。数据保证S中只含有"[", "]", "(", ")" 四种字符
 输出
 每组输入数据的输出占一行，如果该字符串中所含的括号是配对的，则输出Yes,如果不配对则输出No
 */
public class Test1 {

    public static Object arr(int n, String str){
        if(n > 0 && n <= 100 ){
            ArrayList<String> strArr = new ArrayList<>(n);
        }else{
            return "输入出错";
        }
        return null;

    }



    public static String run(String str){
        if(str.charAt(0) == ']' || str.charAt(0) == ')')
            return "no";

        int midFlag = 0;
        int smFlag = 0;
        if(str.charAt(0) == '[')
            midFlag = 1;
        else
            smFlag = 1;

        for(int i = 1; i < str.length(); i++){
            char cflg = str.charAt(i);
            if(midFlag < 0 || smFlag < 0){
                return "no";
            }

            if (midFlag >= 0 && smFlag >= 0){
                if(cflg == ']'){
                    midFlag -= 1;
                }else if(cflg == '['){
                    midFlag += 1;
                }else if(cflg == '('){
                    smFlag += 1;
                }else if(cflg == ')'){
                    smFlag -= 1;
                }
            }
        }
        if(!(midFlag == 0 && smFlag == 0)){
            return "no";
        }
        return "yes";
    }

    public static void main(String[] args) {
        String str = "[([[()]])][]";
        String test = run(str);
        System.out.println(test);
    }
}
