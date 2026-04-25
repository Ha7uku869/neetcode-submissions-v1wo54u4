class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low, high):
            if not root:
                return True
                
            elif not (low < root < high):
                return False
            
            return valid(root.left, low, root) and valid(root.right, root, high)
        valid(root, -float('inf'), float('inf'))