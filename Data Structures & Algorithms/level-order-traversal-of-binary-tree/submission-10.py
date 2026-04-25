# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                tmp = queue.pop(0)
                if not tmp:
                    queue.append(tmp.left)
                    queue.append(tmp.right)
            res.append(queue)
        return res

                


        