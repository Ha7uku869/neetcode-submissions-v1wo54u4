# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot):
        if not subRoot:              # 条件変更
            return True
        if not root:                 # 条件追加
            return False
        if self.isSameTree(root, subRoot):  # チeckして使う！
            return True                        # 見つかったら返す
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))  # 探索！
        
    def isSameTree(self, p, q):
        if not p or not q:
            return False  # ← 明示的にFalse！
        if p.val != q.val:
            return False  # ← 明示的にFalse！