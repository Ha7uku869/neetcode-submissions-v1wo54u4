class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def dfs(left, right):
            if len(s) == 2 * n:
                res.append("".join(s))
                return
            
            if left < n:
                s.append("(")
                dfs(left + 1, right)
                s.pop()

            if right < left:
                s.append(")")
                dfs(left, right + 1)
                s.pop()
            
        dfs(0, 0)
        return res
            