# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        
        
        s = ""
        
        def appending(root,s):
            if root is None:
                return 
            #res.append(str(root.val)+"->")
            
            s = s + "->" + str(root.val)
            
            if (root.left == None and root.right == None):
                res.append(s)
                return 
            
            appending(root.left,s)
            #self.appending(self,root.right)
            appending(root.right,s)
        
        appending(root,s)
        res = [i[2:] for i in res]
        return res
            
            
        
        
        