# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  
        return height
        
    def height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return max(left_h, right_h) + 1

            