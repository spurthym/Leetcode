class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visit=set()
        def search(i,j,p):
            if len(word)==p:
                return True
            if min(i,j)<0 or i>=rows or j>= cols or word[p]!=board[i][j] or (i,j) in visit :
                return False
            visit.add((i,j))
            res=(search(i+1,j,p+1) or search(i-1,j,p+1) or search(i,j+1,p+1) or search(i,j-1,p+1))
            visit.remove((i,j))
            return res
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for i in range(rows):
            for j in range(cols):
                if search(i,j,0):
                    return True
        return False
        