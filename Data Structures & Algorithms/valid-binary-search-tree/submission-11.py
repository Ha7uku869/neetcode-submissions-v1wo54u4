class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low, high):
            if not root:
                return True
                
            elif not (low < root.val < high):
                return False
            
            return valid(root.left, low, root.val) and valid(root.right, root.val, high)

        return valid(root, -float('inf'), float('inf'))