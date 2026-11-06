class Solution:
    def countSmaller(self, nums):
        sorted_nums = sorted(set(nums))
        rank = {x: i + 1 for i, x in enumerate(sorted_nums)}
        n = len(sorted_nums)
        bit = [0] * (n + 1)
        def update(i):
            while i <= n:
                bit[i] += 1
                i += i & -i
        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total
        ans = []
        for x in reversed(nums):
            r = rank[x]
            ans.append(query(r - 1))
            update(r)
        return ans[::-1]
