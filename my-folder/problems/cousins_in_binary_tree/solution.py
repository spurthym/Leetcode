class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        d={}
        def cousin(root,level):
            if not root:
                return
            if root.left and root.right:
                if ((root.left.val == x and root.right.val == y) or 
                    (root.left.val == y and root.right.val == x)):
                    return False

            if root.val==x:
                d[x]=level
            if root.val==y:
                d[y]=level
            
            if len(d)==2 and x in d and y in d:
                if d[x]==d[y]:
                    return True
                else:
                    return False
            
            return cousin(root.left,level+1) or cousin(root.right,level+1)
            
        
        return cousin(root,0)
