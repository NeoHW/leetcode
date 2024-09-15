class MinStack:

    def __init__(self):
        self.standardStack = deque()
        self.minStack = deque() # monotonic decreasing stack: top of stack is always the smallest

    def push(self, val: int) -> None:
        self.standardStack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.standardStack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.standardStack.pop()

    def top(self) -> int:
        return self.standardStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()