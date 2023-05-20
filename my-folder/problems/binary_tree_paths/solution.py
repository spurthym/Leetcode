# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]

        def dfs(root,s):
            if not root:
                return
            

            if root.left==None and root.right==None:
                s=s+"->"+str(root.val)
                l.append(s[2:])
                return

            
            
            dfs(root.left,s+"->"+str(root.val))
            dfs(root.right,s+"->"+str(root.val))
        dfs(root,"")
        return l