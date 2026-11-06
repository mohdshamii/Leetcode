class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        mid = n // 2

        small = sum(x * x for x in nums[:mid])
        large = sum(x * x for x in nums[mid:])

        return large - small
