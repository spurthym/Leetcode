# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        curr=root
        stk=[]
        res=[]

        while curr or stk:
            while curr:
                res.append(curr.val)
                stk.append(curr)
                curr=curr.left

            curr=stk.pop()
            curr=curr.right
        
        return res