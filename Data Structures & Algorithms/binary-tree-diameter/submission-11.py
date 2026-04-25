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
            self.diameter = height(root.left) + height(root.right)
            return max(self.height(root), self.diameter)
        else:
            return self.height(root)
        
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
        
