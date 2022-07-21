# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        second=slow.next
        prev=slow.next=None
        while second:
            temp1=second.next
            second.next=prev
            prev=second
            second=temp1
            
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
            