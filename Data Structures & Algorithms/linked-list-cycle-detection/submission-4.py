# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head.next is not None:
            next_node = head.next
            seen.add(head.val)
            if next_node.val in seen:
                return True
            head = next_node
            
            
        return False

