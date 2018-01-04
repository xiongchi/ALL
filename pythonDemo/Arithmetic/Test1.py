class Test1(object):

    class ListNode:

        def __init__(self, val):
            self.val = val
            self.nodeNext = None

    def __init__(self):
        pass


    def reverse_list(self, head):
        nodePre = None
        while head is not None:
            nodeNext = head.nodeNext
            head.nodeNext = nodePre
            nodePre = head
            head = nodeNext
        return nodePre


if __name__ == '__main__':
    Test1().reverse_list(None)