# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ptr2=head
        dummy=ListNode()
        dummy.next=head
        ptr1=dummy
        while ptr2!=None and ptr2.next!=None:
            
            ptr1=ptr1.next
            ptr2=ptr2.next.next
        
        ptr1.next=ptr1.next.next
        
        return dummy.next