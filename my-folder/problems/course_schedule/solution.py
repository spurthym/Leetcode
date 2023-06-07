from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for j in range(len(prerequisites)):
            d[prerequisites[j][0]].append(prerequisites[j][1])

        def dfs(node):
            visited[node] = True
            stk[node] = True

            for each in d[node]:
                if visited[each] == False:
                    if dfs(each):
                        return True
                elif stk[each] == True:
                    return True
            stk[node] = False
            return False

        visited = [False] * numCourses
        stk = [False] * numCourses

        for k in range(numCourses):
            if not visited[k]:
                if dfs(k):
                    return False
        return True
