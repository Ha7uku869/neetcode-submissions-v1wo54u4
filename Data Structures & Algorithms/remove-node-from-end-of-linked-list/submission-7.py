# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        list_len = 0
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            list_len += 1
        
        reversed_curr = prev

        #reverseする
        while n >= 0:
            n -= 1
            if n == 0:
                if prev.next is None:
                    # 先頭を削除 → どうすればいい？
                    prev = None
                else:
                    prev.next = prev.next.next

        #もう１度reverseする
        curr2 = reversed_curr
        prev2 = None
        while reversed_curr is not None:
            tmp2 = reversed_curr.next
            reversed_curr.next = prev2
            prev2 = reversed_curr
            reversed_curr = tmp2


        return prev2


        
            

