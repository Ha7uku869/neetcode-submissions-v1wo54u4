class MinStack:

    def __init__(self):
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.minStack.pop()
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())
        
        while len(tmp):
            self.stack.append(tmp.pop())

        return mini
        
