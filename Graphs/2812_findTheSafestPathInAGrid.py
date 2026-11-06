'''
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Multi-source BFS
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        def can(k):
            if dist[0][0] < k:
                return False

            vis = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            vis[0][0] = True

            while q:
                x, y = q.popleft()
                if (x, y) == (n - 1, n - 1):
                    return True

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and
                        not vis[nx][ny] and dist[nx][ny] >= k):
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return False

        l, r = 0, max(max(row) for row in dist)

        while l <= r:
            m = (l + r) // 2
            if can(m):
                l = m + 1
            else:
                r = m - 1

        return Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
 

Constraints:

1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
''''''
from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        def can(k):
            if dist[0][0] < k:
                return False
            vis = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            vis[0][0] = True
            while q:
                x, y = q.popleft()
                if (x, y) == (n - 1, n - 1):
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and
                        not vis[nx][ny] and dist[nx][ny] >= k):
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return False
        l, r = 0, max(max(row) for row in dist)
        while l <= r:
            m = (l + r) // 2
            if can(m):
                l = m + 1
            else:
                r = m - 1
        return r
