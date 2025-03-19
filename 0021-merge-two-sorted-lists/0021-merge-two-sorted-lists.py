# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        head = None
        while True:
            new_head = None
            if list1 and (not list2 or list1.val <= list2.val):
                new_head = ListNode(list1.val)
                list1 = list1.next
            elif list2 and (not list1 or list1.val > list2.val):
                new_head = ListNode(list2.val)
                list2 = list2.next
            
            if head:
                head.next = new_head    
                
            head = new_head
            
            if not answer:
                answer = new_head
                
            if not list1 and not list2:
                break
            
        return answer