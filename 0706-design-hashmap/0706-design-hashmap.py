class ListNode:
    def __init__(self, key: Optional[int] = None, value: Optional[int] = None, next: Optional[Self] = None) -> None:
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.size = 10
        self.list: List[ListNode] = [ListNode() for _ in range(self.size)]
        self.load_factor = 0.75
        self.count = 0
        

    def put(self, key: int, value: int) -> None:
        self.do_put(key, value)
                
        if self.isOverloaded():
            self.resize()
            

    def get(self, key: int) -> int:
        node = self.find_node_by_key(key)
        
        if node is not None:
            return node.value
            
        return -1
    

    def remove(self, key: int) -> None:
        prev_node = self.find_prev_node_by_key(key)
        
        if prev_node.next:
            prev_node.next = prev_node.next.next
            

    def do_put(self, key, value):
        node = self.find_prev_node_by_key(key)
        
        while node:
            
            if node.key == key:
                node.value = value
                break
            
            if node.next is None:
                node.next = ListNode(key, value)
                self.count += 1
                
                break

            node = node.next
            

    def resize(self):
        old_size = self.size
        old_list = self.list
        self.size *= 10
        self.list = [ListNode() for _ in range(self.size)]
                    
        for i in range(old_size):
            node = old_list[i]
            
            while node.next:
                self.put(node.next.key, node.next.value)
                node = node.next


    def hash(self, key):
        return key % self.size


    def isOverloaded(self) -> bool:
        return self.size * self.load_factor < self.count
    
    
    def find_node_by_key(self, key):
        return self.find_prev_node_by_key(key).next


    def find_prev_node_by_key(self, key):
        hashed_key = self.hash(key)
        node = self.list[hashed_key]
        prev_node = None
        
        while node:
            
            if node.key == key:
                break
            
            prev_node = node
            node = node.next
            
        return prev_node


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)