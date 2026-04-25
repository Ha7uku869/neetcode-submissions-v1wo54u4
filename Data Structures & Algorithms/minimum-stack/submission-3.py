class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        stack.pop(val)
        
    def top(self) -> int:
        top_num = stack.pop()
        stack.append(top_num)
        return top_num

    def getMin(self) -> int:
        return stack.min()
        
