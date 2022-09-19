# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]
        
        def dfs(root):
            if not root:
                return -1
            l=dfs(root.left)
            r=dfs(root.right)
            res[0]=max(res[0],2+l+r)
            
            return 1+max(l,r)
        dfs(root)
        return res[0]