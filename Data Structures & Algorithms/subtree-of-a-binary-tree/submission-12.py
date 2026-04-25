# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return True
        elif not (root and subRoot) or root.val != subRoot:
            return 
        isSameTree(self, root.left, subRoot.left)
        isSameTree(self, root.right, subRoot.right)
        return 
        
    def isSameTree(self, root, subRoot):
        if not root and subRoot:
            return True
        elif not (root and subRoot) or root.val != subRoot:
            return 
        else:
            return self.isSameTree(root.left, root.right) and self.isSameTree(root.left, root.right)
