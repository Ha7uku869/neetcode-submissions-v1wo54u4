class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        curMax = 0
        while left <= (n - 1):
            seen = set()
            for right in range(left, n):
                if s[right] in seen:
                    seen.add(s[right])
                    curMax = max(curMax, right - left + 1)
                    break
            left += 1
        return curMax