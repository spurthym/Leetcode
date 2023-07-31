# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        curr=head
        dummy=ListNode(-101,None)
        prev=dummy

        while curr:
            if prev.val==curr.val:
                curr=curr.next
                prev.next=curr
                continue
            prev=curr
            curr=curr.next
        return head
        