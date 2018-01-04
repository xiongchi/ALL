package acm;

import java.util.Collections;

/**
 * Created by xiongchi on 2017/12/27.
 * 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
 */
public class Test14 {

    public int JumpFloor(int target) {
        if(target <= 0)
            return 0;
        else if(target == 1)
            return 1;
        else
            return 2*JumpFloor(target - 1);

    }
}
