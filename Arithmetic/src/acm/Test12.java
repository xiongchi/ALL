package acm;

/**
 * Created by xiongchi on 2017/12/25.
 * 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
 * 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
 * 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
 * NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
 */
public class Test12 {

    public int minNumberInRotateArray(int [] array) {

        if (array.length == 0){
            return 0;
        }
        int left = 0;
        int right = array.length - 1;
        int mid = 0;

        while(array[left] >= array[right]){

            if(right - left == 1){
                mid = right;
                break;
            }

            mid = left + (right  - left) / 2;

            //无法知道最小数在那个数组中
            if(array[left] == array[right] && array[left] == array[mid]){
                return midOrder(array, left, right);

            }

            if(array[mid] >= array[left]){
                left = mid;
            }else{
                right = mid;
            }

        }

        return array[mid];

    }


    public int midOrder(int[] arr, int left, int right){
        int result = arr[left];
        for(int i = left+1;i < right; i++){
            if(arr[i] < result){
                result = arr[i];
            }

        }
        return result;

    }

    public static void main(String[] args) {
        int[] a = {6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335};
        System.out.println(new Test12().minNumberInRotateArray(a));
    }



}
