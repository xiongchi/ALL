package acm;


/**
 * Created by xiongchi on 2017/12/22.
 * 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
 * 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
 * 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
 */
public class Test9 {


    /* 先序遍历第一个位置肯定是根节点node，
     
      中序遍历的根节点位置在中间p，在p左边的肯定是node的左子树的中序数组，

      p右边的肯定是node的右子树的中序数组
     
      另一方面，先序遍历的第二个位置到p，也是node左子树的先序子数组，剩下p右边的就是node的右子树的先序子数组
     
      把四个数组找出来，分左右递归调用即可
     
    */
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    public TreeNode reConstructBinaryTree(int[] pre, int[] in) {
        TreeNode root = reConstructBinaryTree(pre, 0, pre.length - 1, in, 0, in.length - 1);
        return root;
    }
   /*
          1
        2   3
      4    5 6
       7  8

    */



    //前序遍历{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}
    private TreeNode reConstructBinaryTree(int[] pre, int startPre, int endPre, int[] in, int startIn, int endIn) {

        if (startPre > endPre || startIn > endIn)
            return null;
        TreeNode root = new TreeNode(pre[startPre]);

        for (int i = startIn; i <= endIn; i++)
            //找到前序遍历和中序遍历的同一个节点
            if (in[i] == pre[startPre]) {
                //当前节点的左孩子节点在前序遍历中肯定在当前位置 到i位置之间 （startPre + 1， startPre + i - startIn） i - startIn 只是表示移动了几位
                //在中序遍历中肯定在当前位置到遍历位置之间（ startIn, i - 1）
                root.left = reConstructBinaryTree(pre, startPre + 1, startPre + i - startIn, in, startIn, i - 1);
                //当前节点的右孩子节点在肯定在当前位置右边也就是pre数组（i - startIn + startPre + 1， endPre）之间
                //在中序遍历中肯定在in数组（i + 1, endIn）位置
                root.right = reConstructBinaryTree(pre, i - startIn + startPre + 1, endPre, in, i + 1, endIn);
                break;
            }

        return root;
    }

    public static void main(String[] args) {
        int[] pre = {1,2,4,7,3,5,6,8};
        int[] in = {4,7,2,1,5,3,8,6};
        Test9 t9 = new Test9();
        System.out.println(t9.reConstructBinaryTree(pre, in));
    }
}
