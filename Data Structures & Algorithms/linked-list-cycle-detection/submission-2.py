# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = ListNode(0)
        seen = set()
        while curr.next == None:
            next_node = curr.next
            seen.add(curr.val)
            if next_node in seen:
                return True
            curr = next_node
            
            
        return False

