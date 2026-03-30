# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow.next
        slow.next = None  # Split the list into two halves
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Now 'prev' is the head of the reversed second half

        # Step 3: Merge the two halves
        first = head
        second = prev
        while second:
            # TODO: Save the next nodes
            next_first = first.next
            next_second = second.next

            # TODO: Link first -> second
            first.next = second

            # TODO: Link second -> next_first
            second.next = next_first

            # TODO: Move pointers forward
            first = next_first
            second = next_second