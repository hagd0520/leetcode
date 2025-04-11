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
        

    # 새로운 키와 값을 입력합니다. 
    # 만약 로드 팩터를 기준으로 과적되어 있을 경우 리사이징을 진행합니다.
    def put(self, key: int, value: int) -> None:
        self.do_put(key, value)
                
        if self.isOverloaded():
            self.resize()
            

    # 입력해둔 데이터 중 인수로 받은 키와 일치하는 데이터의 값을 반환합니다.
    # 키가 일치하는 데이터가 없을 경우 -1을 반환합니다.
    def get(self, key: int) -> int:
        node = self.find_node_by_key(key)
        
        if node is not None:
            return node.value
            
        return -1
    

    # 입력해둔 데이터 중 인수로 받은 키와 일치하는 데이터를 제거합니다.
    # 참조값을 지움으로써 GC에게 수거됩니다.
    def remove(self, key: int) -> None:
        prev_node = self.find_prev_node_by_key(key)
        
        if prev_node.next:
            prev_node.next = prev_node.next.next
            

    # 새로운 키와 값을 입력합니다.
    def do_put(self, key, value) -> None:
        prev_node = self.find_prev_node_by_key(key)
        
        if prev_node.next is None:
            prev_node.next = ListNode(key, value)
            self.count += 1
            
        if prev_node.next is not None:
            prev_node.next.value = value
            

    # 데이터 용량을 열배 늘리고 기존의 데이터들을 이주시킵니다.
    def resize(self) -> None:
        old_size = self.size
        old_list = self.list
        self.size *= 10
        self.list = [ListNode() for _ in range(self.size)]
                    
        for i in range(old_size):
            node = old_list[i]
            
            while node.next:
                self.put(node.next.key, node.next.value)
                node = node.next


    # 간단한 해시 함수입니다.
    def hash(self, key) -> int:
        return key % self.size


    # 데이터가 과적되었는지 여부를 판별합니다.
    def isOverloaded(self) -> bool:
        return self.size * self.load_factor < self.count
    
    
    # 키에 부합하는 데이터의 노드를 반환합니다.
    def find_node_by_key(self, key) -> Optional[ListNode]:
        return self.find_prev_node_by_key(key).next


    # 키에 부합하는 데이터의 이전 노드를 반환합니다.
    def find_prev_node_by_key(self, key) -> ListNode:
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