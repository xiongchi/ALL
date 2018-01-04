package seconde;

import java.util.Random;

/**
 * Created by xiongchi on 2017/10/9.
 */
public class maxsubsum {

    /**
     * 时间复杂度O(N^3)
     * @param a
     * @return
     */
    public static int maxSubSum1(int a[]){
        int maxSum = 0;
        for(int i = 0; i < a.length; i++){
            for(int j = i; j < a.length; j++) {
                int newMaxSum = 0;
                for(int k = i; k <= j; k++){
                    newMaxSum += a[k];
                }
                if(newMaxSum > maxSum){
                    maxSum = newMaxSum;
                }
            }
        }
        return maxSum;
    }

    /**
     * 时间复杂度O(N^2)
     * @param a
     * @return
     */
    public static int maxSubSum2(int a[]){
        int maxSum = 0;
        for (int i = 0; i < a.length; i++) {
            int thisMaxSum = 0;
            for (int j = i; j < a.length; j++) {
                thisMaxSum += a[j];
                if(thisMaxSum > maxSum){
                    maxSum = thisMaxSum;
                }
            }
        }
        return maxSum;
    }

    /**
     * 时间复杂度O(NlogN)
     * @param a
     * @param left
     * @param right
     * @return
     */
    public static int maxSubSum3(int a[], int left, int right){

        if(left == right)
            if(a[left] > 0)
            return a[left];
            else
            return 0;

        int center = (left + right) / 2;


        int leftMax = 0, thisLeftMax = 0;
        for (int i = center; i >= left ; i--) {
            thisLeftMax += a[i];
            if(thisLeftMax > leftMax){
                leftMax = thisLeftMax;
            }
        }

        int rightMax = 0, thisRightMax = 0;
        for (int i = center + 1; i <= right; i++) {
            thisRightMax += a[i];
            if(thisRightMax > rightMax){
                rightMax = thisRightMax;
            }
        }

        int maxLeftSum = maxSubSum3(a, left, center);
        int maxRightSum = maxSubSum3(a, center+1, right);
        return (maxLeftSum > maxRightSum ? maxLeftSum : maxRightSum) > (leftMax + rightMax) ? (maxRightSum > maxLeftSum ? maxRightSum : maxLeftSum) : (leftMax + rightMax);
    }


    /**
     * 时间复杂度O(N)
     * @param a
     * @return
     */
    public static int maxSubnum4(int[] a){
        int maxSum = 0, thisSum = 0;
        for (int i = 0; i < a.length; i++) {
            thisSum += a[i];
            if(thisSum > maxSum){
                maxSum = thisSum;
            }
            else if(thisSum < 0){
                thisSum = 0;
            }
        }
        return maxSum;
    }






    public static int[] getArr(int len){
        Random random = new Random();
        int[] arr = new int[len];
        for(int i =0; i < arr.length; i++){
            arr[i] = random.nextInt(200) - 100;
        }
        return arr;
    }

    public static void main(String[] args) {

//        int arr1[] = {1,-1,3,-10,5,10,-9, 1};
//        int sum = maxSubSum3(arr1,0,arr1.length - 1);
//        System.out.println(sum);

        int arr[] = getArr(5000000);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        Long start = System.currentTimeMillis();
      //  int resSum = maxSubSum3(arr,0 , arr.length -1);
        int resSum = maxSubnum4(arr);
        System.out.println("最大序列和："+resSum);
        Long end = System.currentTimeMillis();
        System.out.println("消耗时间为:"+(end - start)/1000.0);
    }

}
