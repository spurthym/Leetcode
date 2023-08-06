# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        # print(500%8000)
        if not head:
            return None
        curr=head
        ptr2=head
        count=1
        while curr.next:
            count+=1
            curr=curr.next
        k=k%count
        if k==0:
            return head
        

        for i in range(count-k-1):
            ptr2=ptr2.next

        
        temp=ptr2.next
        
        curr.next=head
        ptr2.next=None
        
        return temp


            
        