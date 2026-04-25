class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[right] == '?' or s[right] == '!':
                right -= 1
            elif s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return False
        return True
