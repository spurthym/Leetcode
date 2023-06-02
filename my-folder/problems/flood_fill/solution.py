class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        lrow=len(image)
        lcol=len(image[0])

        stack=[]
        directions=[(+1,0),(-1,0),(0,-1),(0,+1)]
        visited=set()
        oc=image[sr][sc]




        def dfs(row,col):

            for dr,dc in directions:
                r=dr+row
                c=dc+col

                if r in range(lrow) and c in range(lcol) and image[r][c]==oc and (r,c) not in visited:
                    visited.add((r,c))
                    stack.append((r,c))
                    image[r][c]=color
                    dfs(r,c)
                    stack.pop()
        
        image[sr][sc]=color
        stack.append((sr,sc))
        visited.add((sr,sc))
        dfs(sr,sc)
        return image

        





        