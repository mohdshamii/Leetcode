class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        mx, mn = [0] * (n + 1), [float('inf')] * (n + 1)
        d = [0] * n

        for i in range(n):
            mx[i + 1] = max(mx[i], nums[i])
        for i in range(n - 1, -1, -1):
            mn[i] = min(mn[i + 1], nums[i])
        for i in range(1, n):
            d[i] = d[i - 1] + (nums[i - 1] > nums[i])

        def check(k):
            for s in range(0, n, k):
                e = s + k - 1
                if d[e] - d[s] + (nums[e] > nums[s]) > 1 or mx[s] > mn[s]:
                    return False
            return True

        ans = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                ans += i * check(i)
                if i * i != n:
                    ans += (n // i) * check(n // i)
        return ans
