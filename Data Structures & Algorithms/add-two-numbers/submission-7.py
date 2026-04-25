# ファイル名: add_two_numbers.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        count = 0
        v1 = 0
        v2 = 0
        while l1 or l2 or count:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            current.val = (v1 + v2 + count) % 10
            count = (v1 + v2 + count) // 10
            current.next = ListNode(current)

            l1 = l1.next
            l2 = l2.next

        return dummy


            
