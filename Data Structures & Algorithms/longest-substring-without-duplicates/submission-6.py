class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 1
        sub_len = 0
        while j < n:
            if j+1 < n and s[i] == s[j]:
                return j - i
            elif j+1 < n:
                if s[j+1] == s[j]:
                    i = j
                    j = i + 1
                else:
                    j += 1
            elif n == 1:
                return 1
            else: 
                return 0
                

        return j - i