from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        
        for token in tokens:
            if token in operators:
                # 順序が重要なため、先にpopしたものを後方(右側)の被演算子とする
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                if token == '+':
                    ans = left_operand + right_operand
                elif token == '-':
                    ans = left_operand - right_operand
                elif token == '*':
                    ans = left_operand * right_operand
                elif token == '/':
                    # ゼロに向かって切り捨てるために int(a / b) を使用する
                    ans = int(left_operand / right_operand)
                    
                stack.append(ans)
            else:
                # 演算子以外(数字)は整数に変換してスタックに積む
                stack.append(int(token))
                
        # 最後にスタックに残った1つの値が最終結果
        return stack.pop()