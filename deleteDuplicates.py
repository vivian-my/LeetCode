# Definition for singly-linked list.

# 指针赋值 cur 是临时指针 比如她改变了指向节点 head也将改变
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
               
                cur = cur.next
        return head
        