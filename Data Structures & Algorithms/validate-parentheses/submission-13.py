class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        
        # 文字列が空の場合はTrue (問題の定義による)
        if len(s) == 0:
            return True

        for i in range(len(s)):
            char = s[i]

            # 1. 開き括弧ならスタックに追加
            if char == '(' or char == '{' or char == '[':
                stack_list.append(char)
            
            # 2. 閉じ括弧ならチェック
            else:
                # スタックが空なら（対応する開き括弧がない）、即False
                if len(stack_list) == 0:
                    return False
                
                # スタックから取り出す
                top = stack_list.pop()

                # 対応関係をチェック (不一致ならFalse)
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
        
        # 3. ループ終了後、スタックに残っていたら閉じられていないのでFalse
        if len(stack_list) > 0:
            return False
            
        return True