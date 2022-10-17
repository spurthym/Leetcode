# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def isSame(root,l):
            if root==None:
                return 
            if root.left==None and root.right==None:
                l.append(root.val)

            #if root.left:
            isSame(root.left,l)
            #if root.right:
            isSame(root.right,l)
                
        l1 = []
        l2 = []
        a=isSame(root1,l1)
        b=isSame(root2,l2)
        return l1==l2
        