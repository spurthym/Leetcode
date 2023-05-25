from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                live_count = 0

                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] == 1 or board[nr][nc] == -1):
                            live_count += 1

                if board[r][c] == 1 and (live_count < 2 or live_count > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and live_count == 3:
                    board[r][c] = -2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == -2:
                    board[r][c] = 1
