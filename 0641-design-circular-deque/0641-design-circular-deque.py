class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.cap = k + 1
        self.array = [None] * self.cap
        self.front = 0
        self.rear = 0
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.array[self.front] = value
        self.front = self.getPreviousFrontIndex()
        return True

    def insertLast(self, value: int) -> bool:
        print(self.array)
        if self.isFull():
            return False
        self.rear = self.getNextRearIndex()
        self.array[self.rear] = value
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front == self.getNextFrontIndex()
        self.array[self.front] = None
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.array[self.rear] = None
        self.rear = self.getPreviousRearIndex()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.getNextFrontIndex()]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.rear]

    def isEmpty(self) -> bool:
        if self.front == self.rear:
            return True
        return False

    def isFull(self) -> bool:
        if self.getNextRearIndex() == self.front:
            return True
        return False
    
    
    def getNextFrontIndex(self) -> int:
        return (self.front + 1) % self.cap
    
    def getNextRearIndex(self) -> int:
        return (self.rear + 1) % self.cap
    
    def getPreviousFrontIndex(self) -> int:
        return (self.front - 1) % self.cap
    
    def getPreviousRearIndex(self) -> int:
        return (self.rear - 1) % self.cap
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()