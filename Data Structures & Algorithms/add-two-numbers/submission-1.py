# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        while l1 is not None and l2 is not None:
            l1.val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        return head

            