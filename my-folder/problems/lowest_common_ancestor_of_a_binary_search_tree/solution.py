# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path(root,p,q):
            if not root or root==p or root==q:
                return root

            left=path(root.left,p,q)
            right=path(root.right,p,q)

            if left and right:
                return root
            return left or right


        return path(root,p,q)