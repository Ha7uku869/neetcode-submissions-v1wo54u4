# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        k_node = 0
        def in_order(node, k):
            if not node:
                return 0
            in_order(node.left)
            cnt += 1
            if cnt == k:
                k_node = node.val

            in_order(node.right)
            return 0

        return k_node 
                