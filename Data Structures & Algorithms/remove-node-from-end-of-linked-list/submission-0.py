# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        count = 0
        list_len = 0
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            list_len += 1

        while count <= list_len:
            n -= 1
            if n == 0:
                prev.next = prev.next.next
        
        return head

        
            

