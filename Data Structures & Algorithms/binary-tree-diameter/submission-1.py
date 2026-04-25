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
            return max(self.height(root), root.left + root.right)
        else:
            return self.height(root)
        
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(height(root.left), height(root.right)) + 1
    
        
