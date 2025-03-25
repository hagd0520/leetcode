# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        odd_root = head
        even_root = head.next
        
        odd = head
        even = head.next
        
        while even and even.next:
            head = head.next.next
            odd.next = head
            even.next = head.next
            
            odd = odd.next
            if even.next:
                even = even.next
            
        odd.next = even_root
        
        return odd_root