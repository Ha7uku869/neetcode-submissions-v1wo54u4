class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # 左側のポインタが英数字に出会うまでスキップ
            while left < right and not s[left].isalnum():
                left += 1
                
            # 右側のポインタが英数字に出会うまでスキップ
            while left < right and not s[right].isalnum():
                right -= 1
                
            # 両方を小文字に変換して比較。一致しなければ回文ではない
            if s[left].lower() != s[right].lower():
                return False
            
            # 次の文字へ進む
            left += 1
            right -= 1
            
        # 最後まで矛盾がなければ回文として判定
        return True