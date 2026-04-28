class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        curMax = 0
        while left <= (n - 1):
            for right in range(left, n):
                curMax = max(curMax, right - left)
            left += 1
        return curMax