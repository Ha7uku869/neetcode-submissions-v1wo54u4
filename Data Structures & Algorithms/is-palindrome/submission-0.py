class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)//2):
            stack.append(s[i])
        for j in reversed(range(len(s))):
            if stack.pop() == s[j]:
                continue
            else:
                return False

        return True
        