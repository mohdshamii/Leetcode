class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # N, E, S, W
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacle_set = set(map(tuple, obstacles))
        x = y = 0
        d = 0
        ans = 0
        for command in commands:
            # turn left
            if command == -2:
                d = (d + 3) % 4
            # turn right
            elif command == -1:
                d = (d + 1) % 4
            # move
            else:
                dx, dy = dirs[d]
                for _ in range(command):
                    nx = x + dx
                    ny = y + dy
                    # obstacle → stop this command
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)
        return ans
