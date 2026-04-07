# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt, k_node = 0, 0
        
        def in_order(node):
            nonlocal cnt, k_node
            if not node:
                return 
            in_order(node.left)
            cnt += 1
            if cnt == k:
                k_node = node.val
                return 
            in_order(node.right)
            return 
        in_order(root)

        return k_node 
                