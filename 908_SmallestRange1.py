 class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)

        return max(0, (mx - k) - (mn + k))
