class Solution:
    def smallestIndex(self, nums):
        for i, n in enumerate(nums):
            if sum(map(int, str(n))) == i:
                return i
        return -1
