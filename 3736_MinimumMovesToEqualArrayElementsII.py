class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        return mx * len(nums) - sum(nums)
