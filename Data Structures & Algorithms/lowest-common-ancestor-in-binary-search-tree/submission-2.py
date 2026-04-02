# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        if p.val > q.val:
            p, q = q, p
        while cur.val:
            if cur.val < p.val:
                cur = cur.right
            elif q.val < cur.val:
                cur = cur.left
            else:
                return cur
            


