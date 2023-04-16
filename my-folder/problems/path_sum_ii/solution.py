# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        curr=root
        temp=[]
        s=0
        def ps(curr,s):
            if curr==None:
                
                
                return 
            
            temp.append(curr.val)
            s+=curr.val
            if s==targetSum and curr.left==None and curr.right==None:   
                res.append(temp.copy())
            ps(curr.left,s)
            ps(curr.right,s)
            temp.pop()
            s-=curr.val
           
        res=[]
        ps(curr,s)
        return res