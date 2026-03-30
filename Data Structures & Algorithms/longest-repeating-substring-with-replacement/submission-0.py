class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # 各文字の出現回数を管理
        left = 0
        max_len = 0

        for right in range(len(s)):
            # 1. s[right]をcountに追加
            # dictで「あれば+1、なければ1」の書き方
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. 条件チェック
            while (right - left + 1) - max(count.values()) > k:
                # ウィンドウが無効 → leftを縮める
                count[s[left]] -= 1
                left += 1
            
            # 3. 最大長を更新
            max_len = max(max_len, right - left + 1)

        return max_len
            