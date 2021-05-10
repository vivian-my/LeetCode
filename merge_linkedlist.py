# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# input = [1,2,3] and [2,3,4]
# output = [1,2,2,3,3,4]

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        while l2 and l1:
                if l2.val < l1.val:
                    head.next = l2
                    l2=l2.next
                else:
                    head.next = l1
                    l1 = l1.next
                head = head.next
        head.next=l1 if l1 is not None else l2
        return first.next

# method : recursive

    def mergeTwoLists_2(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
