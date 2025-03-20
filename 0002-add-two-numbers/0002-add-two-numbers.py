# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = l1
        carry = 0
            
        while l1 or l2:
            
            if not l1:
                l1 = ListNode()

                
            if carry:
                l1.val += 1
                carry -= 1
                
            if l2:
                l1.val += l2.val
            
            if l1.val >= 10:
                l1.val -= 10
                carry += 1
            
            if not l1.next and not l2.next:
                break
            
            if not l1.next:
                l1.next = ListNode()
                
            if not l2.next:
                l2.next = ListNode()
                
            l1 = l1.next
            l2 = l2.next
            
            
        if carry:
            l1.next = ListNode(1)
            
        return answer