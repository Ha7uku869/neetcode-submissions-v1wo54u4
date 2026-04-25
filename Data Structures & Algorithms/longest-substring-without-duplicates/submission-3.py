class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 1
        while j < n:
            if n == 0:
                return 0
            elif n == 1:
                return 1
            if s[i] == s[j]:
                return j - i
            else:
                j += 1
        return j - 1