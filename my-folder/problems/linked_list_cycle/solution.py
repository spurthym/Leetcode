# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow,fast=head,head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

            if fast==slow:
                return True
        return False
        '''
        d=set()
        ptr1=head

        while ptr1:
            if ptr1 in d:
                return True
            
            d.add(ptr1)
            ptr1=ptr1.next
        return False'''