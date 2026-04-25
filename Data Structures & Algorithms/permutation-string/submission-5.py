class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub = {}
        i = 0
        for k in range(len(s1)):
            sub[s1[k]] = sub.get(s1[k], 0) + 1  
            sub_sub = sub.copy()    

        while i < len(s2):
            sub_sub = sub
            if s2[i] in sub_sub:
                for j in range(len(s2)):
                    sub_sub[s2[i + j]] -= 1
                if len(sub_sub) == 0:
                    return True
            i += 1
        
        return False
        
