"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldtonew={}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            copy=Node(node.val)
            oldtonew[node]=copy

            for each in node.neighbors:
                copy.neighbors.append(dfs(each))
            return copy
        return dfs(node) if node else None
