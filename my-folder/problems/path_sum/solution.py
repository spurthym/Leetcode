# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False

        def path(root,s):
            print(s)
            print()
            if root==None:   
                return
            if s+root.val==targetSum and (root.left==None and root.right==None):
                print("ret",s)
                return True
            return path(root.left,s+root.val) or path(root.right,s+root.val)
        
        return path(root,0)
           
