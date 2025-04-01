class MyStack:

    def __init__(self):
        self.f_deque = deque()
        self.s_deque = deque()
        

    def push(self, x: int) -> None:
        while self.f_deque:
            self.s_deque.append(self.f_deque.popleft())
            
        self.f_deque.append(x)
        
        while self.s_deque:
            self.f_deque.append(self.s_deque.popleft())
        

    def pop(self) -> int:
        return self.f_deque.popleft()
        

    def top(self) -> int:            
        return self.f_deque[0]
        

    def empty(self) -> bool:
        return not bool(self.f_deque)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()