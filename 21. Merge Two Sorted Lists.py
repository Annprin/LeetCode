# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        curr = head
        while list1 or list2:
            if not list1 or list2 and list1.val > list2.val:
                tmp = list2
                list2 = list2.next
            else:
                tmp = list1
                list1 = list1.next
            curr.next = tmp
            curr = tmp
        return head.next