class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) != 0 :
            if self.minStack[-1] > val:
                self.minStack.append(val)
        self.stack.append(val)


    def pop(self) -> None:
        if len(self.stack) != 0:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            cur = self.tack.pop()
            

    def top(self) -> int:
        return self.minStack[-1]
    
        

    def getMin(self) -> int:
        return self.minStack[-1] 
