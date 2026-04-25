class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        stack.push(val)

    def pop(self) -> None:
        stack.pop(val)
        
    def top(self) -> int:
        top_num = stack.pop()
        stack.push(top_num)
        return top_num

    def getMin(self) -> int:
        return stack.min()
        
