# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        
        def one_way_dfs(node, max_val):
            nonlocal cnt

            if not node:
                return

            if node.val >= max_val:
                cnt += 1

            new_max = max(max_val, node.val)

            one_way_dfs(node.left, new_max)
            one_way_dfs(node.right, new_max)

        one_way_dfs(root, root.val)

        return cnt