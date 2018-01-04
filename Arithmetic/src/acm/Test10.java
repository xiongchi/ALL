package acm;

import java.util.ArrayList;
import java.util.LinkedList;

/**
 * 创建二叉树 和 遍历二叉树
 * Created by xiongchi on 2017/12/22.
 */
public class Test10 {
    static class TreeNode{
        TreeNode left;
        TreeNode right;
        int data;
        TreeNode(int data){
            this.data = data;
        }
    }

    public static LinkedList<TreeNode> create(ArrayList<Integer> arr){

        LinkedList<TreeNode> linkedList = new LinkedList<>();

        for(int i = 0; i < arr.size(); i++){
            TreeNode t = new TreeNode(arr.get(i));
            linkedList.add(t);
        }
        int parentIndex;
        for(parentIndex = 0; parentIndex < linkedList.size() / 2 - 1; parentIndex++){

            linkedList.get(parentIndex).left = linkedList.get(parentIndex * 2 + 1);

            linkedList.get(parentIndex).right = linkedList.get(parentIndex * 2 + 2);

        }

        linkedList.get(linkedList.size() / 2 - 1).left = linkedList.get(2 * (linkedList.size() / 2 - 1) + 1);
        //判断是否有右孩子节点 长度为奇数才有右孩子节点
        if(linkedList.size() % 2 == 1){
            linkedList.get(linkedList.size()/2 - 1).right = linkedList.get(2 * (linkedList.size() / 2 - 1) + 2);
        }
        return linkedList;
    }

    //先序遍历
    public static void preOrder(TreeNode node){
        if(node == null){
            return;
        }
        System.out.println(node.data);
        preOrder(node.left);
        preOrder(node.right);
    }

    //中序遍历
    public static void inOrder(TreeNode node){
        if(node == null){
            return;
        }

        preOrder(node.left);
        System.out.println(node.data);
        preOrder(node.right);
    }


    //后序遍历
    public static void postOrder(TreeNode node){
        if(node == null){
            return;
        }

        preOrder(node.left);
        preOrder(node.right);
        System.out.println(node.data);
    }


    public static void main(String[] args) {
        int[] a = {1,3,4,57,12,34,56,322,5};
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i : a){
            arr.add(i);
        }
        LinkedList<TreeNode> list = create(arr);
        TreeNode root = list.get(0);
        preOrder(root);
        System.out.println("-------------------------------");
        inOrder(root);
        System.out.println("-------------------------------");
        postOrder(root);


    }



}
