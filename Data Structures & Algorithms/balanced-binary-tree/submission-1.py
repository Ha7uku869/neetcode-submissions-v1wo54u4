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
        elif not root.right and not root.left:
            self.cnt += 1
        elif not root.right and root.left or root.right and not root.left:
            if cnt == 2:
                return False
        return isBalanced(root.right) and isBalanced(root.left)
            