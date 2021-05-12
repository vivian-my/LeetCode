# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#利用数组可以反着查原理
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val = []
        cur = head
        while cur:
            val.append(cur.val)
            cur = cur.next
        return val == val[::-1]