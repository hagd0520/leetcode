class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.size = k + 1
        self.array = [None for i in range(self.size)]
    

    def enQueue(self, value: int) -> bool:
        temp = self.front + 1
        if temp >= self.size:
            temp = 0
            
        if temp == self.rear:
            return False
        
        self.front = temp
        
        self.array[self.front] = value
        return True
        

    def deQueue(self) -> bool:
        if self.front == self.rear:
            return False
        self.rear += 1
        if self.rear >= self.size:
            self.rear = 0
        self.array[self.rear] = None
        return True
        

    def Front(self) -> int:
        temp = self.rear + 1
        if temp >= self.size:
            temp = 0
        var = self.array[temp]
        if var is None:
            return -1
        return var
        

    def Rear(self) -> int:
        var = self.array[self.front]
        if var is None:
            return -1
        return var
        

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.Front() is -1:
            return True
        return False
            

    def isFull(self) -> bool:
        temp = self.front + 1
        if temp >= self.size:
            temp = 0
        if temp == self.rear and self.Front() is not -1:
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