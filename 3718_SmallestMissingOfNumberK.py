class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)

        multiple = k

        while multiple in s:
            multiple += k

        return multiple
