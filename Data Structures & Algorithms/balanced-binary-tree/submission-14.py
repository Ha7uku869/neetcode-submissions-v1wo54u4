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
        self.height(root)
        return  self.result
        
    def height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        if abs(left_h - right_h) > 1:
            self.result = False

        return max(left_h, right_h) + 1

            