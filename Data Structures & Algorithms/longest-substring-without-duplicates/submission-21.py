# filename: solution.py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # s[right] が seen に存在する間、重複が解消されるまで left の文字を削除し続ける
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # 新しい文字を seen に追加し、最大長を更新
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length