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
        res.append([root.val])
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while queueが空でない間:
            level_size = len(queue)
            for i in range(level_size):
                tmp = queue.pop(0)
                queue.append(tmp.left)
                queue.append(tmp.right)
            res.append(queue)
        return res

                


        