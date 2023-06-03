from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i in range(numCourses):
            d[i] = []
        for j in range(len(prerequisites)):
            d[prerequisites[j][0]].append(prerequisites[j][1])

        visited = set()
        memo = {}

        def isfinishable(node):
            if node in visited:
                return False
            if node in memo:
                return memo[node]
            visited.add(node)
            for j in d[node]:
                if not isfinishable(j):
                    memo[node] = False
                    visited.remove(node)
                    return False
            visited.remove(node)
            memo[node] = True
            return True

        for each in d:
            if not isfinishable(each):
                return False

        return True
