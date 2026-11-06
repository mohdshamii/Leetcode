class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if grid[r][c] == "0":
                return

            # Mark visited
            grid[r][c] = "0"

            # 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count
