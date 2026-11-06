class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
