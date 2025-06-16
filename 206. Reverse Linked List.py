# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmp = head
        prev = None
        while tmp:
            next_node = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next_node
        return prev