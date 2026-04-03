class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, open_cnt, close_cnt):
            if len(cur) == 2 * n:
                res.append(cur)
                return                          # ← ここで終わり。それだけ。

            if open_cnt < n:
                backtrack(cur + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(cur + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)   # ← backtrackの外、generateParenthesisの中
        return res             # ← backtrackの外、generateParenthesisの中