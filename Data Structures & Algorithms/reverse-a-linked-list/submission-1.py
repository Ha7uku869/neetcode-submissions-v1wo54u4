# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
                prev = None
                current = head
                next_node = 0
                while current != None:
                    next_node = current.next
                    ListNode.next = None
                    current.next = prev
                    prev = current 
                    current = next=node
