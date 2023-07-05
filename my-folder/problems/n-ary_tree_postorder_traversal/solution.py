"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def pt(root):
            if root is None:
                return
          
            if root.children is None:
                res.append(root.val) 
         
                return
            for each in root.children:
            
                pt(each)
          
            res.append(root.val)
        pt(root)
        return res

