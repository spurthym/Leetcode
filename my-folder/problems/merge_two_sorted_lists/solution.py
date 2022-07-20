# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1=list1
        t2=list2
        t3=ListNode()
        dummy=t3
        
        while t1 and t2:
            if t1.val<t2.val:
                dummy.next=t1
                t1=t1.next
            else: 
                dummy.next=t2
                t2=t2.next
            dummy=dummy.next
        
        if t1:
            dummy.next=t1
        else:dummy.next=t2
                
        return t3.next

            