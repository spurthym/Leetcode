# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        slow=fast=head
        while fast is not None and fast.next is not None:
            temp=slow
            fast=fast.next.next
            slow=slow.next
        temp.next=slow.next
        
                
        
        
        
        return head
        