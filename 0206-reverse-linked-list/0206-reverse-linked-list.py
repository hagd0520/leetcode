# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        while True:
            next = None
            if head:
                next = head.next
                head.next = temp
                temp = head
            
            if not next:
                break
            
            head = next         

        return temp