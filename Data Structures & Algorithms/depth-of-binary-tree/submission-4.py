# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        cnt = 0
        max_cnt = 0
        def dfs(node):
            nonlocal cnt, max_cnt
        
        cnt += 1
        max_cnt = max(cnt, max_cnt)
        
        self.maxDepth(root.left)
        self.maxDepth(root.right)

        return max_cnt
