package acm;

/**
 * Created by xiongchi on 2018/1/3.
 */
public class Test20 {

    public static class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public static ListNode Merge(ListNode list1,ListNode list2) {
        ListNode merage = null;
        if(list1 == null && list2 == null){
            return null;
        }else if(list1 == null && list2 != null){
            return list2;
        }else if(list1 != null && list2 == null){
            return list1;
        }
        ListNode p = new ListNode(0);
        merage = p;
        //使用两个变量是 使用p来记录头节点
        while(list1 != null && list2 != null){
            if(list1.val > list2.val){
                merage.next = list2;
                list2 = list2.next;
                merage = merage.next;

            }else{
                merage.next = list1;
                list1 = list1.next;
                merage = merage.next;
            }

        }

        if(list1 != null){
            merage.next = list1;
        }
        if(list2 != null){
            merage.next = list2;
        }

        return p.next;

    }


    /**
     * 根据两个链表递归 知道为null res 没有遍历 所以一个变量就够了
     * @param list1
     * @param list2
     * @return
     */
    public static ListNode diGui(ListNode list1,ListNode list2){

        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }
        ListNode res = null;
        if(list1.val < list2.val){
            res = list1;
            res.next = diGui(list1.next, list2);
        }else{
            res = list2;
            res.next = diGui(list1, list2.next);
        }
        return res;
    }

    public static void main(String[] args) {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(3);
        list1.next.next = new ListNode(5);

        ListNode list2 = new ListNode(2);
        list2.next = new ListNode(4);
        list2.next.next = new ListNode(6);

        ListNode merage = Merge(list1, list2);

        while(merage != null){
            System.out.println(merage.val);
            merage = merage.next;
        }

    }
}
