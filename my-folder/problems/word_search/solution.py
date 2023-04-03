class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows=len(board)
        cols=len(board[0])
        visit=set()        


        def backtrack(i,j,k):
            if k==len(word):
                return True
            
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!=word[k] or (i,j) in visit :
                return False
            
            visit.add((i,j))
            res=(
            backtrack(i+1,j,k+1) or
            backtrack(i-1,j,k+1) or
            backtrack(i,j+1,k+1) or 
            backtrack(i,j-1,k+1))

            visit.remove((i,j))
            return res
        

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0): return True
        
        return False
