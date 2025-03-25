# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = head
        
        for i in range(left - 1):
            head = head.next
            
        left_head = head
        
        head = root
        
        for i in range(right - 1):
            head = head.next
        
        prev = head.next
        
        head = root
        
        for i in range(right - left):
            next = left_head.next
            
            left_head.next = prev
            
            prev = left_head
            
            left_head = next
            
        left_head.next = prev
        
        if left == 1:
            return left_head
        
        for i in range(left - 2):
            head = head.next
        
        head.next = left_head
            
        return root