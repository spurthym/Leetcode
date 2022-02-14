# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy=ListNode()
        
        dummy.next=head
    
        count=0
        counter=dummy
        
        while counter:
            count=count+1
            counter=counter.next
        
            
        curr=dummy
        nn=count-n-1
        
        for i in range(0,nn):
            curr=curr.next
        curr.next=curr.next.next
        
        return dummy.next 