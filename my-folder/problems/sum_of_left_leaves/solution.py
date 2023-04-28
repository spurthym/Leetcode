# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        s=0

        def dfs(root):
            nonlocal s
            if root==None:
                return
            if root.left and root.left.left==None and root.left.right==None:
                s+=root.left.val
            

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return s        
