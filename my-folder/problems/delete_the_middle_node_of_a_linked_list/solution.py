# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast=head
        dummy=ListNode(0,head)
        slow=dummy
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
        