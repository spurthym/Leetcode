# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        

        slow=head
        fast=head
        dummy=ListNode(-1,head)
        prev=dummy

        while fast and fast.next:
        
            fast=fast.next.next

            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        if fast:
            slow=slow.next
            

        while slow:

            if slow.val==prev.val:
                prev=prev.next
                slow=slow.next
            else:
                return False
            
        if prev.val==-1:
            return True
        return False