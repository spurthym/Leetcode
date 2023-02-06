class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])

        directions=[[-1,0],[1,0],[0,-1],[0,1]]

        p_queue=deque()
        a_queue=deque()

        for i in range(rows):
            p_queue.append((i,0))
            a_queue.append((i,cols-1))

        for c in range(cols):
            p_queue.append((0,c))
            a_queue.append((rows-1,c))

        def bfs(q):
            reachable=set()
            while(q):
                row,col=q.popleft()
                # col=
                # while(q):
                reachable.add((row,col))
                for ro,co in [[-1,0],(1,0),(0,-1),(0,1)]:
                    new_r=row+ro
                    new_c=col+co

                
                    if new_r>=rows or new_r<0 or new_c>=cols or new_c <0:
                        continue
                    if (new_r,new_c) in reachable:
                        continue
                    if  heights[new_r][new_c]<heights[row][col]:
                        continue
                    q.append((new_r,new_c))
            return reachable
            
        
            


            
        



        p_reachable=(bfs(p_queue))
        a_reachable=(bfs(a_queue))
        print(p_reachable)
        print()
        print(a_reachable)
        return list(p_reachable.intersection(a_reachable))
        

        # # Check if input is empty
        # if not matrix or not matrix[0]: 
        #     return []
            
        # num_rows, num_cols = len(matrix), len(matrix[0])

        # # Setup each queue with cells adjacent to their respective ocean
        # pacific_queue = deque()
        # atlantic_queue = deque()
        # for i in range(num_rows):
        #     pacific_queue.append((i, 0))
        #     atlantic_queue.append((i, num_cols - 1))
        # for i in range(num_cols):
        #     pacific_queue.append((0, i))
        #     atlantic_queue.append((num_rows - 1, i))
        
        # def bfs(queue):
        #     reachable = set()
        #     while queue:
        #         (row, col) = queue.popleft()
        #         # This cell is reachable, so mark it
        #         reachable.add((row, col))
        #         for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
        #             new_row, new_col = row + x, col + y
        #             # Check if the new cell is within bounds
        #             if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
        #                 continue
        #             # Check that the new cell hasn't already been visited
        #             if (new_row, new_col) in reachable:
        #                 continue
        #             # Check that the new cell has a higher or equal height,
        #             # So that water can flow from the new cell to the old cell
        #             if matrix[new_row][new_col] < matrix[row][col]:
        #                 continue
        #             # If we've gotten this far, that means the new cell is reachable
        #             queue.append((new_row, new_col))
        #     return reachable
        
        # # Perform a BFS for each ocean to find all cells accessible by each ocean
        # pacific_reachable = bfs(pacific_queue)
        # atlantic_reachable = bfs(atlantic_queue)

    
           
                
