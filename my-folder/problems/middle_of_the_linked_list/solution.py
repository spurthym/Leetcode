# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next==None:
            return head
        else:
        
            curr=head
            count=0
            f=None
            while curr:
                count=count+1
                curr=curr.next
            for i in range(0,int(count/2)):
                    f=head.next
                    head=head.next
            return f
            
            
                
        