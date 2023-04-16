# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s=0

        def dfs(curr):
         
            if curr==None:
                return

            total=0
            nonlocal s

            if curr.val%2==0:
                if curr.left and curr.left.left:
                    total+=curr.left.left.val
                    print("s1",s)
                if curr.left and curr.left.right:
                    total+=curr.left.right.val
                    print("s2",s)
         
                if curr.right and curr.right.left:
                    total+=curr.right.left.val
                    print("s3",s)
          
                if curr.right and curr.right.right:
                    total+=curr.right.right.val
                    print("s4",s)
            s+=total
            dfs(curr.left)
            dfs(curr.right)

            
        
        dfs(root)
        return s

