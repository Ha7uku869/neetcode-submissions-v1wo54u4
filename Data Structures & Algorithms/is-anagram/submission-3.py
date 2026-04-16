class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        seen = defaultdict(lambda: 0)
        if len_s != len_t:
            return False
        for i in range(len_s):
            seen[s[i]] += 1

        for j in range(len_s):
            if seen[t[j]] == 0:
                return False
            else:
                seen[t[j]] -= 1
        return True
        
