# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#两个链表 输出相交的node 值

#又是环的思路 快慢指针 一定会相遇 把最后的tail指向头 形成环

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None:
            return None
        if headB is None:
            return None
        n_1 = headA
        n_2 = headB
        while n_1!=n_2:
            if n_1==None:
                n_1 = headB
            else:
                n_1 = n_1.next
            if n_2 == None:
                n_2 = headA
            else:
                n_2 = n_2.next
        return n_2



