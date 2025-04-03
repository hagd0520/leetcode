class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.size = k 
        self.cap = k + 1
        self.array = [None] * self.cap
            

    def enQueue(self, value: int) -> bool:            
        if self.isFull():
            return False
                
        self.rear = (self.rear + 1) % self.cap
        self.array[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        self.array[self.front] = None
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[(self.front + 1) % self.cap]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.rear]
        

    def isEmpty(self) -> bool:
        if self.front == self.rear:
            return True
        return False
            

    def isFull(self) -> bool:
        if (self.rear + 1) % self.cap == self.front:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()