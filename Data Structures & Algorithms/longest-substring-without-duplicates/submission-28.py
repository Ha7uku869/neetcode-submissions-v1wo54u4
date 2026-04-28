class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        curMax = 0
        seen = set()
        while left <= (n - 1):
            for right in range(left, n):
                if s[right] in seen:
                    seen.add(s[right])
            left += 1
        return curMax