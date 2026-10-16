from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = s = 0
        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                res = tree[node]
                length = r - l + 1
                tree[node] += length
                lazy[node] += 1
                return res
            mid = (l + r) // 2
            lc, rc = node * 2, node * 2 + 1
            if lazy[node]:
                v = lazy[node]
                tree[lc] += (mid - l + 1) * v
                tree[rc] += (r - mid) * v
                lazy[lc] += v
                lazy[rc] += v
                lazy[node] = 0
            res = 0
            if ql <= mid:
                res += update(lc, l, mid, ql, qr)
            if qr > mid:
                res += update(rc, mid + 1, r, ql, qr)
            tree[node] = tree[lc] + tree[rc]
            return res
        for i, x in enumerate(nums, 1):
            p = last.get(x, 0)
            s = (s + 2 * update(1, 1, n, p + 1, i) + i - p) % MOD
            ans = (ans + s) % MOD
            last[x] = i
        return ans
