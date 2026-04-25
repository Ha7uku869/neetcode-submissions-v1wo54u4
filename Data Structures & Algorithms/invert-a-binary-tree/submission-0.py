# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        while root:
            root = TreeNode()
            tmp = root.right
            root.right = root.left
            root.left = tmp
            return root.left
            return root.right
        return root
