# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=head
        prev=dummy
        while curr and curr.next:
            t1=curr.next
            t2=curr.next.next
            
            t1.next=curr
            curr.next=t2
            prev.next=t1
            
            prev=curr
            curr=t2
        return dummy.next
        