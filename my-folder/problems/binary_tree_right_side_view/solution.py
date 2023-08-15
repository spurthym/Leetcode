# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        res=[]

        q=deque()
        q.append(root)
        while q:
            q_len=len(q)
            for i in range(q_len):
                curr=q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i ==q_len-1:
                    res.append(curr.val)
        return res
            