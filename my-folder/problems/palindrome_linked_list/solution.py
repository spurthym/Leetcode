# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        stk=[]
        while fast and fast.next:
            stk.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
            


        while slow and stk:

            if slow.val==stk[-1]:
                stk.pop()
                slow=slow.next
            else:
                return False
        
        if len(stk)>0:
            return False
    
        return True

