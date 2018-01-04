package acm;

/**
 * Created by xiongchi on 2017/12/28.
 */
public class Test16 {

    public double Power(double base, int exponent) {
        return Math.pow(base, exponent);
    }

    public static void main(String[] args) {
        System.out.println(new Test16().Power(22.0, 330));
    }
}
