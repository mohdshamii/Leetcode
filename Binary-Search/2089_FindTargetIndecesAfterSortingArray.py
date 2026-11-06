#1ST SOLN
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]
 #2nd soln

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

        return ans

