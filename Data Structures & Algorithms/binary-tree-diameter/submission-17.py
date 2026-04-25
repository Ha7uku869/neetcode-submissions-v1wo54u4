# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def height(root):
            if not root:
                return 0
            diameter = (height(root.left) - 1) + (height(root.right) - 1)
            return max(height(root.left), height(root.right)) + 1
        height(root)
        return diameter
            