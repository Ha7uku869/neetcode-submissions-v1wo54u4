"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        current = dummy
        while current:
            current.next.val = head.val
            current.next = head.next
            current.next.random = head.random
            current = current.next

        return dummy.next


