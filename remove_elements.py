# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
    
        pre = ListNode(-1)
        pre.next = head
        cur = pre

        if head is None:
            return head

        while cur:
            if cur.next and cur.next.val ==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
    
        return pre.next