class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 対応する括弧のマッピング（閉じ括弧 → 開き括弧）
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # 開き括弧の場合
                stack.append(char)
            elif char in mapping:          # 閉じ括弧の場合
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                return False  # 不正な文字
        
        return not stack  # スタックが空ならTrue