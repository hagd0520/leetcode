class ListNode:
    def __init__(self, key: Optional[int] = None, value: Optional[int] = None, next: Optional[Self] = None) -> None:
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.size = 10
        self.list: List[ListNode] = [ListNode()] * self.size
        self.load_factor = 0.75
        self.count = 0
        

    def put(self, key: int, value: int) -> None:
        hashed_key = self.hash(key)
        exist_node = self.list[hashed_key]
        while exist_node:
            
            if exist_node.key == key:
                exist_node.value = value
                return
            
            if exist_node.next is None:
                exist_node.next = ListNode(key, value)
                return

            exist_node = exist_node.next
                    

    def get(self, key: int) -> int:
        hashed_key = self.hash(key)
        exist_node = self.list[hashed_key]
        
        while exist_node:
            
            if exist_node.key == key:
                return exist_node.value
            
            if exist_node.next is None:
                break
            
            exist_node = exist_node.next
            
        return -1

        
    def remove(self, key: int) -> None:
        hashed_key = self.hash(key)
        exist_node = self.list[hashed_key]
        prev_node: Optional[ListNode] = None
        
        while exist_node:
            if exist_node.key == key:
                prev_node.next = prev_node.next.next
                return
            
            prev_node = exist_node
            exist_node = exist_node.next

        
    def hash(self, key):
        return key % self.size


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)