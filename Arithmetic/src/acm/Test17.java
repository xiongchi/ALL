package acm;

import java.util.ArrayList;

/**
 * Created by xiongchi on 2017/12/28.
 */
public class Test17 {
    public void reOrderArray(int [] array) {
        int len = array.length;
        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> b = new ArrayList<>();
        for(int i = 0; i < len; i++){
            if(array[i] % 2 == 0){
                a.add(array[i]);
            }else{
                b.add(array[i]);
            }
        }

        b.addAll(a);
    }
}
