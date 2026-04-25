class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right = 0, 1
        seen = set()
        seen.add(s[0])
        cnt = 1
        maxCnt = 1
        while right < len(s):
            if s[right] in seen:
                left += 1
                maxCnt = max(cnt, maxCnt)
                cnt = 1
                seen = set()
                seen.add(s[left])
            else:
                cnt += 1
                seen.add(s[right])
            right += 1
        maxCnt = max(cnt, maxCnt)
        return maxCnt
                    

                
