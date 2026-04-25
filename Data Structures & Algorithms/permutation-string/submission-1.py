class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub = set()
        i = 0
        for k in range(len(s1)):
            sub.add(s1[k])
        
       

        while i < len(s2):
            sub_sub = sub
            if s2[i] in sub_sub:
                for j in range(len(s2)):
                    sub_sub.remove(s2[i + j])
                if len(sub_sub) == 0:
                    return True
            i += 1
        
        return False
        
