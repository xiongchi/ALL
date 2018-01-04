package acm;

import java.util.ArrayList;

/**
 * Created by xiongchi on 2017/12/29.
 */
public class Test18 {
    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode FindKthToTail(ListNode head,int k) {

        ArrayList<ListNode> arr = new ArrayList<>();
        for(;head != null; head = head.next){
            arr.add(head);
        }
        if(arr.size() - k < 0 || k == 0){
            return null;
        }
        return arr.get(arr.size() - k);
    }
}
