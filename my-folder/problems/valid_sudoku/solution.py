class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        grid=defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c]==".":
                    continue
                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c]
                or board[r][c] in grid[r//3,c//3]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r//3,c//3)].add(board[r][c])
        return True