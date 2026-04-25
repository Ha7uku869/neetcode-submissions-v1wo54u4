class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 1
        sub_len = 0
        while j < n:
            if j+1 < n - 1:
                if j+2 < n - 1 and s[j+1] == s[j]:
                    i = j + 1
                    j = i + 1
                else:
                    j += 1
            elif n == 1:
                return 1
            else: 
                return 0
                

        return j - i