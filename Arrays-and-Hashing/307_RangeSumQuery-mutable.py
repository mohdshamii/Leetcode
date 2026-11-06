class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i, x in enumerate(nums):
            self._update(i + 1, x)

    def _update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _query(self, i):
        total = 0

        while i > 0:
            total += self.bit[i]
            i -= i & -i

        return total

    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val

        self._update(index + 1, delta)

    def sumRange(self, left, right):
        return self._query(right + 1) - self._query(left)
