# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        else:
            return True
        
    def height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        left_h = height(root.left)
        right_h = height(root.right)

        return max(left_h, right_h) + 1

            