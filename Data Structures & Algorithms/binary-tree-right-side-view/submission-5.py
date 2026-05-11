from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        while q:
            cur_level = len(q)
            for i in range(cur_level):
                node = q.deque()
                if node.left:
                    q.append([node.left])
                if node.right:
                    q.append([node.right])
                if i == cur_level - 1:
                    res.append(node.val)
            

        return res