class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        halfStack = []
        if n % 2 == 1:
            return False
        for i in range(n // 2):
            halfStack.append(s[i])
        for j in range(n // 2, n):
            if halfStack.pop() == '(' and s[j] == ')':
                return True
            elif halfStack.pop() == '{' and s[j] == '}':
                return True
            elif halfStack.pop() == '[' and s[j] == ']':
                return True
            else:
                return False
            
        if halfStack is None:
            return True
        else:
            return False


        


        