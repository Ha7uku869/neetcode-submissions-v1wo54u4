class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)
        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return False
        return True
