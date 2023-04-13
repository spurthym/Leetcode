"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def depth(root):
            if root==None:
                return 0
            ans=0

            for i in range(len(root.children)):
                tempans=depth(root.children[i])
                ans=max(ans,tempans)
            return ans+1
        return depth(root)
        