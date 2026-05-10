# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 1
        
        def one_way_dfs(root, max_val):
            nonlocal cnt
            if not root:
                return
            if not root.left and not root.right:
                return cnt
            if root.left and root.left.val < max_val or root.right and root.right.val < max_val:
                cnt += 1
            one_way_dfs(root.left, max(root.left.val, root.val))
            one_way_dfs(root.left, max(root.right.val, root.val))
            
            return
        one_way_dfs(root, root.val)

        return cnt