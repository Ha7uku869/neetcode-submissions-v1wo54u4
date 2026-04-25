# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        self.isSameTree(self, root.left, subRoot.left)
        self.isSameTree(self, root.right, subRoot.right)
        return False
        
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not (root and subRoot) or root.val != subRoot:
            return 
        else:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
