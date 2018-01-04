package acm;

import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by xiongchi on 2017/12/22.
 * 输入一个链表，从尾到头打印链表每个节点的值。
 */
public class Test8 {

    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }


    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (; listNode != null; listNode = listNode.next) {
            arr.add(listNode.val);
        }
        Collections.reverse(arr);
        return arr;
    }


}
