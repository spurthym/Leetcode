class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows validation
        rows=defaultdict(set)
        cols=defaultdict(set)
        grid=defaultdict(set)

        for i in range(9):
            for j in range(9):
                spos=(i//3*3+j//3)
                print(spos)
                if board[i][j]==".":
                    continue
                elif board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in grid[spos]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grid[spos].add(board[i][j])
        return True





        