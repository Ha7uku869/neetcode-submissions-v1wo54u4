class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        if n == 0:
            return 0
        left = 0
        
        while left <= (n - 1):
            seen = set()
            seen.add(s[left])
            cnt = 1
            for right in range(left + 1, n):
                ans = max(ans, cnt)
                if s[right] in seen:
                    break
                seen.add(s[right])
                cnt += 1
            ans = max(ans, cnt)

                    
            left += 1
        return ans


