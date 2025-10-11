class MyQueue:

    def __init__(self):
        self.in_stk = [] # in_stk: push here
        self.out_stk = [] # out_stk: pop/peek here

    def push(self, x: int) -> None:
        self.in_stk.append(x)
    
    def _move_from_in_to_out_stack(self) -> None:
        # putting into in_stk from out_stk reverse out_stk -> queue order
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

    def pop(self) -> int:
        self._move_from_in_to_out_stack()
        return self.out_stk.pop()

    def peek(self) -> int:
        self._move_from_in_to_out_stack()
        return self.out_stk[-1]
        

    def empty(self) -> bool:
        return not self.in_stk and not self.out_stk
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()