# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        while True:
            print(list1)
            if list1 and (not list2 or list1.val >= list2.val):
                answer.append(list1.val)
                list1 = list1.next
            
            if list2 and (not list1 or list1.val < list2.val):
                answer.append(list2.val)
                list2 = list2.next
                
            if not list1 and not list2:
                break
            
        return answer