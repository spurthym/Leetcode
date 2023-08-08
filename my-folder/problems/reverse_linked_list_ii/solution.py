# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        lefthead=dummy
        l=head
        for i in range(left-1):
            l=l.next
            lefthead=lefthead.next
        prev=None
        for i in range(right-left+1):
            print(i)
            curr=l.next
            l.next=prev
            prev=l
            l=curr
        lefthead.next.next=curr
        lefthead.next=prev
        
        return dummy.next
