# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        elem=[]
        
        if not root:
            return []
        
  
        elem+=self.inorderTraversal(root.left)
            
        elem.append(root.val)
        
      
        elem+=self.inorderTraversal(root.right)

            
    
        
        
        
        
        return elem
    '''   
        class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s=[]  #array to append the visited nodes
        s+=(self.inorderTraversal(root.left))  #using recursive call to traverse the left nodes
        s+=[root.val]
        s+=(self.inorderTraversal(root.right)) #using recursive calls to traverse the right nodes
        return s
        ''' 