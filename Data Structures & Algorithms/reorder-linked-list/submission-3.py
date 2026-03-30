from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # ステップ1: 真ん中を見つける（slow/fast pointer）
        slow, fast = head, head
        while fast and fast.next:   # ← A: fast が None になる前に止める条件
            slow = slow.next
            fast = fast.next.next        # ← B: fast を2つ進める

        # ステップ2: 後半を逆順にする（slow が中間ノード）
        second = slow.next
        slow.next = None   # 前半と後半を切り離す
        prev = None
        while second:
            tmp = second.next
            second.next = prev # ← C: reverseの核心
            prev = second
            second = tmp

        # ステップ3: 前半と逆順後半をマージする
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next =  second # ← D: firstの次に後半の先頭を挿入
            first.next.next = tmp1  # ← E: その次に前半の続きをつなぐ
            first = tmp1
            second = tmp2      # ← F: 後半を進める