class MinStack:
    def __init__(self):
        stack = []
        minStack = []

    def push(self, val: int) -> None:
        if len(stack) == 0:
            stack.append(val)
        else:
            if minStack[-1] > val:
                minStack.append(val)
        stack.append(val)


    def pop(self) -> None:
        if len(stack) != 0:
            if stack[-1] == minStack[-1]:
                minStack.pop()
            cur = stack.pop()
            

    def top(self) -> int:
        return stack[-1]
    
        

    def getMin(self) -> int:
        minValue  = minStack[-1] 
