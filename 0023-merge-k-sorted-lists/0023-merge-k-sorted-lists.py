# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        
        _list = []
        for i in lists:
            while i:
                _list.append(i.val)
                i = i.next
        
        _list.sort()
        
        head = root
        
        for i in _list:
            head.next = ListNode()
            head = head.next
            head.val = i
            
        return root.next