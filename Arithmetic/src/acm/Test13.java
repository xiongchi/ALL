package acm;

/**
 * Created by xiongchi on 2017/12/27.
 * 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
 */
public class Test13 {

    public int Fibonacci(int n) {
        if(n <= 1)
            return n;
        else
            return Fibonacci(n - 1) + Fibonacci(n + 1);
    }

    public int Fibonacci2(int n) {
        if (n <= 1)
            return n;
        int[] arr = new int[n + 1];
        arr[0] = 0;
        arr[1] = 1;
        for(int i = 2;i <= n; i++){
            arr[i] = arr[i - 1] + arr[i - 2];
        }
        return arr[n];
    }
}
