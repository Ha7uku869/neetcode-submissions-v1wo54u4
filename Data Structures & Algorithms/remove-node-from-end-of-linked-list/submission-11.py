class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ① 反転
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        reversed_head = prev

        # ② 前から n 番目を削除
        dummy = ListNode(0, reversed_head)
        curr = dummy

        for _ in range(n - 1):   # ←ここが重要
            curr = curr.next

        # 削除
        curr.next = curr.next.next

        # ③ もう一度反転
        curr = dummy.next
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev