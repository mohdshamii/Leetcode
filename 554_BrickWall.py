class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}

        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                edges[pos] = edges.get(pos, 0) + 1

        return len(wall) - max(edges.values(), default=0)
