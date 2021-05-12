# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#删除一个给定节点，需要得到上一个节点 但是得不到 所以可以把下一个节点赋值给删除节点 再删除下一个节点

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next=node.next.next