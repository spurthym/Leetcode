# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q=collections.deque()
        q.append(root)
        res=[]
        
        while q:
            level=[]
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    res.append(node.val)
        return len(res)