class Solution:
    def floodFill(self, img: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(img)
        cols=len(img[0])
        directions=[[0,-1],[0,1],[-1,0],[1,0]]
        visit=set()

        org=img[sr][sc]
        q=collections.deque()
        q.append((sr,sc))
        visit.add((sr,sc))
        img[sr][sc]=color

        while q:
            ro,co=q.popleft()
            for dr,dc in directions:
                r=ro+dr
                c=co+dc

                if r in range(rows) and c in range(cols) and (r,c) not in visit and img[r][c]==org:
                    q.append((r,c))
                    visit.add((r,c))
                    img[r][c]=color
        return img


        