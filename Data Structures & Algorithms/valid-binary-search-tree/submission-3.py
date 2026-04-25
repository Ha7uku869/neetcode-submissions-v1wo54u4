# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif root.left and root.right:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        elif root.left and not root.right:
            return self.isValidBST(root.left)
        elif not root.left and root.right:
            return self.isValidBST(root.right)
        else:
            return False
            