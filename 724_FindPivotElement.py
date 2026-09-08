class Solution:
    def pivotIndex(self, nums):
        n = len(nums)
        for i in range(n):
            left_sum = 0
            right_sum = 0
            for j in range(i):
                left_sum += nums[j]
            for j in range(i + 1, n):
                right_sum += nums[j]
            if left_sum == right_sum:
                return i
        return -1
