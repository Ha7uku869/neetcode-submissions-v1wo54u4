class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        ans = 0
        for i in range(len(tokens)):
            if tokens[i] in operators:
                if tokens[i] == '+':
                    ans = stack.pop() + stack.pop()
                elif tokens[i] == '-':
                    ans = stack.pop() - stack.pop()
                elif tokens[i] == '*':
                    ans = stack.pop() * stack.pop()
                else:
                    tokens[i] == '/'
                    ans = stack.pop() // stack.pop()
                stack.push(ans)
            else:
                stack.push(tokens[i])
        return stack.pop()
                
        