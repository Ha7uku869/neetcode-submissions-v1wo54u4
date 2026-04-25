class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        seen = set()
        seen.append(s[0])
        cnt = 1
        maxCnt = 1
        if len(s) == 0:
            return 0
        while right < len(s):
            if s[right] in seen:
                left = right
                maxCnt = max(cnt, maxCnt)
            else:
                cnt += 1
                seen.append(s[right])
            right += 1
        return maxCnt
                    

                
