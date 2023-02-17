# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk=[]
        res=[]
        cur=root
        while cur or stk:
            while cur:
                stk.append(cur)
                res.append(cur.val)
                cur=cur.left
            cur=stk.pop()
            
            cur=cur.right
        
        return res
        '''
        elem=[]
        
        if not root:
            return []
        
        elem.append(root.val)

        elem+=self.preorderTraversal(root.left)
            
        elem+=self.preorderTraversal(root.right)
        
        return elem
        '''