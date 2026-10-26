class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            val = grid[r][c]
            grid[r][c] = 0

            val += dfs(r + 1, c)
            val += dfs(r - 1, c)
            val += dfs(r, c + 1)
            val += dfs(r, c - 1)

            return val

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total = dfs(i, j)
                    if total % k == 0:
                        ans += 1

        return ans
