class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        top_num = self.stack.pop()
        self.stack.append(top_num)
        return top_num

    def getMin(self) -> int:
        sorted_stack = sorted(self.stack)
        return sorted_stack[0]
        
