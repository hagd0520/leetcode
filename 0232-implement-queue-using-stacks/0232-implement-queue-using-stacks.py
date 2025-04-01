class MyQueue:

    def __init__(self):
        self.f_stack = []
        self.s_stack = []
        
        
    def push(self, x: int) -> None:
        while self.f_stack:
            self.s_stack.append(self.f_stack.pop())
        self.f_stack.append(x)
        
        while self.s_stack:
            self.f_stack.append(self.s_stack.pop())
        

    def pop(self) -> int:
        return self.f_stack.pop()
        

    def peek(self) -> int:
        return self.f_stack[-1]
        

    def empty(self) -> bool:
        return not bool(self.f_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()