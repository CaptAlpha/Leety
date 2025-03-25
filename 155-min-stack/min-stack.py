class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.minArray = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)


    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
