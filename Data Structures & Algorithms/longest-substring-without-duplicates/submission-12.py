class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        max_len = 0

        for right in range(len(s)):
            # s[right] が重複している間、左を縮める
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            # s[right] をウィンドウに追加
            window.add(s[right])
            
            # 現在のウィンドウ長と最大値を比較
            max_len = max(max_len, right - left + 1)

        return max_len