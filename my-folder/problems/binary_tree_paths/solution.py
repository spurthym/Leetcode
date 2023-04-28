class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def path(root, s):
            if not root:
                return
            
            s += str(root.val)
            if not root.left and not root.right:
                res.append(s)
                return
            
            s += "->"
            path(root.left, s)
            path(root.right, s)
        
        path(root, "")
        return res
