from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Build the adjacency list representation of the graph
        adj_list = defaultdict(list)
        degrees = [0] * n

        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
            degrees[x] += 1
            degrees[y] += 1

        # Perform topological sorting starting from the leaves
        leaves = deque()
        for i in range(n):
            if degrees[i] == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves

            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in adj_list[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)

        # The remaining nodes are the root(s) of the minimum height trees
        return list(leaves)
