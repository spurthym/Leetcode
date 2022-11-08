# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def helper(node,left,right):
            if not node:
                return True
            
            if not (node.val<right and node.val>left):
                return False
            return (helper(node.left,left,node.val) and helper(node.right,node.val,right))
        return helper(root,-math.inf,math.inf)
        
        

        '''
        def helper(temp):
            if temp.left==None and temp.right==None:
                return True
            if temp.left==None:
                return helper(temp.right)
            if temp.right==None:
                return helper(temp.left)
                
            
            
            if  (temp.left.val<temp.val and temp.right.val>temp.val):
                return helper(temp.left) and helper(temp.right)
                
            else:
                return False
        return helper(root)
        
        
            
            
        '''