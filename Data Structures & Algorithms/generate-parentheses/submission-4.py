class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, open_cnt, close_cnt):
            # 1. ゴール → res に追加して return
            if len(cur) == 2 * n:
                res.append(cur)
                return  backtrack("", 0, 0)      # ← これも大事！ゴールしたらそれ以上探索しない

            # 2. "(" を選べるなら → 再帰で探索
            if open_cnt < n:
                backtrack(cur + "(", open_cnt + 1, close_cnt)  # ← 再帰！

            # 3. ")" を選べるなら → 再帰で探索
            if close_cnt < open_cnt:
                backtrack(cur + ")", open_cnt, close_cnt + 1)  # ← 再帰！

            return res