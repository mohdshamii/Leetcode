class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1
        best = [INF] * n
        left = 0
        curr = 0
        min_len = INF
        ans = INF
        for right in range(n):
            curr += arr[right]
            while curr > target:
                curr -= arr[left]
                left += 1
            if curr == target:
                length = right - left + 1
                if left > 0:
                    ans = min(ans, length + best[left - 1])
                min_len = min(min_len, length)
            best[right] = min_len
        return -1 if ans == INF else ans
