class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            a, b = 0, 0
            if token == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
            
        return stack.pop()
            
                
        