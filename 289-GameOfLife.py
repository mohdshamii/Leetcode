class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for i in range(m):
            for j in range(n):
                live = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] == 1 or board[ni][nj] == 2:
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2      # live -> dead
                else:
                    if live == 3:
                        board[i][j] = 3      # dead -> live

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
