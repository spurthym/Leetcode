# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        
        l=[]
        def inorder(self,root):
            if not root:
                return None
            inorder(self,root.left)
            l.append(root.val)
            inorder(self,root.right)
            return l
        inorder(self,root)
        
        newTree=TreeNode(l[0])
        temp=newTree
        
        for i in range(1,len(l)):
            newNode=TreeNode(l[i])
            temp.right=newNode
            temp=temp.right
            
        return newTree
        