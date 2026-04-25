# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        curr = head
        while head.next is not None:
            while curr.next is not None:
                curr = curr.next
            next_node = head.next
            head.next = curr
            head = head.next
            head.next = next_node
        