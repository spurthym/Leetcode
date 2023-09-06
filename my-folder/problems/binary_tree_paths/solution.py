# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]

        def dfs(root,s):
            if not root:
                return
            s=s+str(root.val)
            
            if not root.left and not root.right:
            
                res.append(s)
                
                return
            s+="->"
            
            dfs(root.left,s)
        
            dfs(root.right,s)
        dfs(root,"")
        return res