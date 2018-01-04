package acm;

/**
 * Created by xiongchi on 2017/12/29.
 */
public class Test19 {

    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode ReverseList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode next = null;
        ListNode pre = null;
        while(head != null){
            next = head.next;
            head.next = pre;

            pre = head;
            head = next;
        }
        return pre;
    }
}
