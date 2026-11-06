class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        if nums == sorted(nums):
            return 0

        k = (1 << n.bit_length()) - 1

        for i, x in enumerate(nums):
            if i != x:
                k &= x

        return k
