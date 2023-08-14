# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        level=1
        q=deque()
        res=[]
        q.append(root)

        while q:
            s=0
            div=len(q)
            for i in range(len(q)):
                curr=q.popleft()
                s+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            res.append(s/div)
           
        return res
        
        