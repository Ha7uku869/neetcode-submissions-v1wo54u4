from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = Counter(t)            # tの必要文字カウント
        window = defaultdict(int)    # ウィンドウ内のカウント

        have, required = 0, len(need)
        res, res_len = [-1, -1], float("inf")  # float("inf") は無限大

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            # 追加でちょうど必要回数に達したときだけhaveを増やす
            if c in need and window[c] == need[c]:
                have += 1

            # 条件を満たしている間、左を縮められるだけ縮める
            while have == required:
                # 最短更新の判定
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # 左端を窓から外す
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""