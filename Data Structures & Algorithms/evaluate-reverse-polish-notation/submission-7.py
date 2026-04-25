class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            a, b = 0, 0
            if token == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(b + a)
            elif token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(b * a)
            elif token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(b // a)
        return tokens.pop()
            
                
        