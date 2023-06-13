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
        min_nodes=math.inf
        
        def depth(root,n):
            nonlocal min_nodes
            if root==None:
                return
            if root.left==None and root.right==None:
                if n<min_nodes:
                    min_nodes=n
                return
            depth(root.left,n+1)
            depth(root.right,n+1)
        depth(root,1)
        return min_nodes

