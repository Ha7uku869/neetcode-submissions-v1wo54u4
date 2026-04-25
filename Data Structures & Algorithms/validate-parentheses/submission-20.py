class Solution:
    def isValid(self, s: str) -> bool:
        halfStack = []
        if len(s) == 0:
            return True
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                halfStack.append(s[i])
            elif len(s) == 0:
                return False
            elif s[i] != stack.pop():
                return False
        
                