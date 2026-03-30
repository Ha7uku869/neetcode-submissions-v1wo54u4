class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # fastをn+1進める
        for i in range(n + 1):
            fast = fast.next

        # 同時に進める
        while fast:
            fast = fast.next
            slow = slow.next

        # 削除
        slow.next = slow.next.next

        return dummy.next