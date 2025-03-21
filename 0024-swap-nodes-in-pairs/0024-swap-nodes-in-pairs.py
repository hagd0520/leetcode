# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = None
        prev = None
        
        if not head or not head.next:
            return head
        
        while True:
            if not head or not head.next:
                break
            
            left = head
            right = head.next
            head = head.next.next
            
            if prev:
                prev.next = right
                
            right.next = left
            left.next = head
            
            prev = left
            
            if not root:
                root = right
                
        return root