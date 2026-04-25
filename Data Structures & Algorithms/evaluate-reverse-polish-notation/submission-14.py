class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        if len(tokens) == 0:
            return 0
        for i in range(len(tokens)):
            if tokens[i].isalnum():
                stack.append(int(tokens[i]))
            elif len(stack) == 0 or len(stack) == 1:
                return False
            elif tokens[i] == '+':
                ans = stack.pop() + stack.pop()
            elif tokens[i] == '-':
                ans = - stack.pop() + stack.pop()
            elif tokens[i] == '*':
                ans = stack.pop() * stack.pop()
            else:
                ans = 1 // stack.pop() * stack.pop()
            stack.append(ans)
        return ans

                


        