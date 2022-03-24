# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.ismirror(root.left, root.right )
    def ismirror(self,lr,rr):
        
        if lr and rr:
            return lr.val==rr.val and self.ismirror(lr.left,rr.right) and self.ismirror(lr.right,rr.left)
        
        return lr==rr
    
        