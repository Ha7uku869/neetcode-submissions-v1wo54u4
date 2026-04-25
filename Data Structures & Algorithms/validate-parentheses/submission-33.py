class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            elif len(stack) == 0 and (s[i] == ']' or s[i] == '}' or s[i] == ')'):
                return False
            stack.pop()
                    
        if len(stack) != 0:
            return False
        return True
                


