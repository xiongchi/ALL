package seconde;

/**
 * Created by xiongchi on 2017/10/26.
 */
public class binarysearch {

    public static int binarySearch_1(int[] a, int num){

        int low = 0, high = a.length - 1;

        while( low <= high ){
            int mid = (low + high) /  2;

            if( a[mid] < num){
                low = mid + 1;
            }else if(a[mid] > num){
                high = mid - 1;
            }
            return mid;
        }
        return -1;
    }


}
