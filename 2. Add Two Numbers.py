# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        one = 0
        head = ListNode()
        ptr = head
        if not l1:
            return l2
        elif not l2:
            return l1

        while l1 or l2 or one:
            l1 = l1 if l1 else ListNode()
            l2 = l2 if l2 else ListNode()
            val = l1.val + l2.val + one
            one = val // 10
            val %= 10
            tmp = ListNode(val=val)
            ptr.next = tmp
            ptr = tmp
            l1 = l1.next
            l2 = l2.next
        return head.next