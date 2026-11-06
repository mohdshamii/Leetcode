class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            x = num % k
            ndp = [0] * k

            ndp[x] += 1

            for r in range(k):
                nr = (r * x) % k
                ndp[nr] += dp[r]

            dp = ndp

            for r in range(k):
                ans[r] += dp[r]

        return ans
