# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head
        max_s=0
        while fast is not None:

            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        while curr !=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        
        while prev:
            max_s=max(max_s,head.val+prev.val)

            head=head.next
            prev=prev.next
        
        return max_s
        
        