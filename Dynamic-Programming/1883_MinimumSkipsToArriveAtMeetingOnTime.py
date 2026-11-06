class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = 10**18

        # dp[j] = minimum scaled time using exactly j skips
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n - 1):
            ndp = [INF] * (n + 1)

            for skips in range(i + 1):
                if dp[skips] == INF:
                    continue

                # 1. Skip the rest
                ndp[skips + 1] = min(
                    ndp[skips + 1],
                    dp[skips] + dist[i]
                )

                # 2. Don't skip the rest
                time = dp[skips] + dist[i]

                rounded = ((time + speed - 1) // speed) * speed

                ndp[skips] = min(
                    ndp[skips],
                    rounded
                )

            dp = ndp

        # Last road: no rounding/rest after it
        for skips in range(n):
            total = dp[skips] + dist[-1]

            if total <= hoursBefore * speed:
                return skips

        return -1
