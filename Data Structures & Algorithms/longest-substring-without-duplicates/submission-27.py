class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        curMax = 0
        seen = set()
        while left <= (n - 1):
            for right in range(left, n):
                if seen[right] in s:
                    seen.add(s[right])
            left += 1
        return curMax