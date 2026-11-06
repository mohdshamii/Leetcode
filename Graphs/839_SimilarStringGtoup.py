from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        def is_similar(a: str, b: str) -> bool:
            diff = 0

            for c1, c2 in zip(a, b):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False

            return True

        for i in range(n):
            for j in range(i + 1, n):
                if find(i) != find(j) and is_similar(strs[i], strs[j]):
                    union(i, j)

        return sum(find(i) == i for i in range(n))
