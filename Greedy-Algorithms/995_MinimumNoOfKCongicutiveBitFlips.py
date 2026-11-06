class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flip = 0
        ans = 0
        for i in range(n):
            if i >= k and nums[i - k] == 2:
                flip ^= 1
            if nums[i] == flip:
                if i + k > n:
                    return -1
                nums[i] = 2
                flip ^= 1
                ans += 1
        return ans
