# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.right is None and root.left is not None:
            return root.left
        elif root.right is not None and root.left is None:
            return root.right
        elif root.right is None and root.left is None:
            return 1 
        
        self.maxDepth(root.left)
        self.maxDepth(root.right)

        return maxDepth(root.left) + maxDepth(root.right)
