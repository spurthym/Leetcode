from collections import defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        visited = set()

        def dfs(source):
            visited.add(source)

            if destination in d[source]:
                return True

            for each in d[source]:
                if each not in visited:
                    if dfs(each):
                        return True
            return False

        d = defaultdict(list)
        for i in range(n):
            d[i] = []

        for j in range(len(edges)):
            d[edges[j][0]].append(edges[j][1])
            d[edges[j][1]].append(edges[j][0])

        if dfs(source):
            return True 
        else:
            return False
