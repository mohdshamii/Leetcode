from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        class BIT:
            def __init__(self, n):
                self.n = n
                self.t = [0] * (n + 1)

            def add(self, i, v):
                while i <= self.n:
                    self.t[i] += v
                    i += i & -i

            def query(self, i):
                s = 0
                while i:
                    s += self.t[i]
                    i -= i & -i
                return s

            def kth(self, k):
                i = 0
                bit = 1 << (self.n.bit_length() - 1)
                while bit:
                    nxt = i + bit
                    if nxt <= self.n and self.t[nxt] < k:
                        i = nxt
                        k -= self.t[nxt]
                    bit >>= 1
                return i + 1

        counts = BIT(m)
        sums = BIT(m)
        window_sum = 0
        cost = [0] * (n - x + 1)

        def add(v, delta):
            nonlocal window_sum
            r = rank[v]
            counts.add(r, delta)
            sums.add(r, v * delta)
            window_sum += v * delta

        def get_cost():
            med_rank = counts.kth((x + 1) // 2)
            med = vals[med_rank - 1]
            left_count = counts.query(med_rank)
            left_sum = sums.query(med_rank)
            return med * left_count - left_sum + (window_sum - left_sum) - med * (x - left_count)

        for i in range(x):
            add(nums[i], 1)

        for i in range(n - x + 1):
            cost[i] = get_cost()
            if i + x < n:
                add(nums[i], -1)
                add(nums[i + x], 1)

        inf = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            cur = [inf] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] != inf:
                    cur[i] = min(cur[i], prev[i - x] + cost[i - x])
            prev = cur

        return prev[n]
