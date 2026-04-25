class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while s[left].isalnum():
                left += 1
            while s[right].isalnum():
                right -= 1
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            
