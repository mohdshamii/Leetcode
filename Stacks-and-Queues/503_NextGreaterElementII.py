class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                j = stack.pop()
                ans[j] = nums[idx]
            if i < n:
                stack.append(idx)
        return ans
