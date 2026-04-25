class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        if len(s) == 1:
            return 1
        for left in range(len(s)):
            tmp = k
            cur_len = 1
            right = left + 1
            max_len = max(max_len, cur_len)
            while tmp >= 0 and right < len(s):
                if s[left] != s[right]:
                    tmp -= 1
                right += 1
                cur_len += 1
        return max_len




