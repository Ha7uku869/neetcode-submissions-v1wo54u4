class MinStack:
    def __init__(self):
        stack = []
        minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            stack.append(val)
        else:
            if minStack[-1] > val:
                minStack.append(val)
        self.stack.append(val)


    def pop(self) -> None:
        if len(self.stack) != 0:
            if self.stack[-1] == minStack[-1]:
                minStack.pop()
            cur = stack.pop()
            

    def top(self) -> int:
        return self.stack[-1]
    
        

    def getMin(self) -> int:
        minValue  = minStack[-1] 
