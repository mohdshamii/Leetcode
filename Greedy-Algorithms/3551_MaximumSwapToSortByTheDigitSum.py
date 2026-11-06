class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(arr)}
        seen = set()
        ans = 0
        for i in range(len(nums)):
            if i in seen:
                continue
            j = i
            cycle = 0
            while j not in seen:
                seen.add(j)
                j = pos[nums[j]]
                cycle += 1
            ans += max(0, cycle - 1)
        return ans
