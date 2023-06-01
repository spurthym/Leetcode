from typing import List
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        q = deque()

        def dfs(node, temp):
            if node == len(graph) - 1:
                res.append(temp + [node])
                return

            for next_node in graph[node]:
                dfs(next_node, temp + [node])

        dfs(0, [])
        return res
