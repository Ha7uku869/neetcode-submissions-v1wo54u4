class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len, cur_len = 1, 1
        tmp = k #この処理の仕方わからん
        for left in range(len(s)):
            right = left + 1
            max_len = max(max_len, cur_len)
            while k >= 0:
                if s[left] != s[right]:
                    if k > 1:
                        right += 1
                    k -= 1
                cur_len += 1
        return max_len




