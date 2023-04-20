# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        res=0
        q=deque([[root,1,0]])
        prevlevel=0
        prevnum=1


        while q:
            
            curr,num,level=q.popleft()
            if level>prevlevel:
                prevlevel=level
                prevnum=num
            res=max(res,num-prevnum+1)
      
            
            if curr.left:
                q.append((curr.left,num*2,level+1))
              
            if curr.right:
                q.append((curr.right,num*2+1,level+1))
            

        return res
        
