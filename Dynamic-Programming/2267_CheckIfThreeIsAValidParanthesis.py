class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2:
            return False
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        for i in range(m):
            for j in range(n):
                for balance in dp[i][j]:
                    if i + 1 < m:
                        nb = balance + (1 if grid[i + 1][j] == '(' else -1)
                        if nb >= 0:
                            dp[i + 1][j].add(nb)
                    if j + 1 < n:
                        nb = balance + (1 if grid[i][j + 1] == '(' else -1)
                        if nb >= 0:
                            dp[i][j + 1].add(nb)
        return 0 in dp[m - 1][n - 1]
