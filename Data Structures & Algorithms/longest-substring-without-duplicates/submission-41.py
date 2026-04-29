class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        print(n)
        ans = 0
        if n == 0:
            return 0
        left = 0
        while left <= (n - 1):
            cnt = 1
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    ans = max(ans, cnt)
                    print(ans)
                    break
                else:
                    cnt += 1
            left += 1
        return ans


