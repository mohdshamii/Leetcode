from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                overlap = 0

                for r in range(n):
                    for c in range(n):
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            overlap += img1[r][c] & img2[nr][nc]

                ans = max(ans, overlap)

        return ans
