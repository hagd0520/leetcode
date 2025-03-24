# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        count = 0
        
        while head:
            count += 1
            if count % 2 == 1:
                odd.append(head)
            else:
                even.append(head)
            
            head = head.next
            
        odd_and_even = odd + even
        
        root = head = ListNode()
        
        for i in odd_and_even:
            head.next = i
            head = i
            
        head.next = None
            
        return root.next