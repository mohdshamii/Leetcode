class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        right[0][0] = 1
        for i in range(m):
            for j in range(n):
                r = right[i][j]
                d = down[i][j]
                if grid[i][j] == 0:
                    ways = (r + d) % MOD
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + ways
                        ) % MOD
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + ways
                        ) % MOD
                else:
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + r
                        ) % MOD
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + d
                        ) % MOD
        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD
