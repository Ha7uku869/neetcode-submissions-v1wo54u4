# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head is not None:
            next_node = head.next
            seen.add(head)
            if next_node in seen:
                return True
            head = next_node
            
            
        return False

