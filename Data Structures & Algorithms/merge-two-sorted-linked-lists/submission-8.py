# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)  # ダミーノード
        curr = dummy         # 結果リストの末尾を追跡

        # list1もlist2も存在する間はどちらを追加するか比較
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1    # 小さい方をつなぐ
                list1 = list1.next        # list1を進める
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next         # currを進める

        # どちらかが残っている場合
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next              # ダミーの次が先頭