class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            c[i][0] = c[i][i] = 1
            for j in range(1, i):
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
        def solve(arr):
            if len(arr) <= 2:
                return 1
            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]
            ways = c[len(left) + len(right)][len(left)]
            return ways * solve(left) % MOD * solve(right) % MOD
        return (solve(nums) - 1) % MOD
