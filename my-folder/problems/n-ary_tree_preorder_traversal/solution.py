"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
      
        if not root:
            return []
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            for i in range(len(node.children)-1,-1,-1):
                if node.children[i]:
                    stack.append(node.children[i])
        return result
