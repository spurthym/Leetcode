# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1=head
        d={}

        while ptr1:
            if ptr1 in d:
                return ptr1
            

            d[ptr1]=0
            ptr1=ptr1.next
        return None
        