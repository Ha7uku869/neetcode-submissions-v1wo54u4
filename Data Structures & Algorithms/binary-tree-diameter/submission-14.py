# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.right and root.left:
            
            return self.result
        else:
            return self.height(root) - 1
        
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        self.result = max(self.result, left_h + right_h)
        return max(left_h, right_h) + 1
    
        
