# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        min_depth=math.inf

        q=deque()
        q.append(root)
        nodes=1
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                if curr.left==None and curr.right==None:
                    return nodes
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            nodes+=1
        

        