# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        li=[]
        addr=head

        while True:
            if addr == None:
                return False
                break
            if addr not in li:
                li.append(addr)
                addr=addr.next
            else:
                return True
        
    
        
    