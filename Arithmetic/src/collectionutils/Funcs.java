package collectionutils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

/**
 * Created by xiongchi on 2017/12/27.
 */
public class Funcs {

    class Books implements Comparable{
        public int id;
        public String name;


        @Override
        public int compareTo(Object o) {
            Books b = (Books) o;
            return this.id - b.id;
        }
    }


    public static void mySort(){
        Double array[] = {new Double(112), new Double(111), new Double(23)};
        ArrayList<Double> list = new ArrayList<Double>(Arrays.asList(array));
        Collections.sort(list);
        System.out.println(list);
    }

    public static void main(String[] args) {
        mySort();
    }
}
