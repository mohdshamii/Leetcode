
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(diff) <= k:
            return 0
        left, right = 0, max(diff)
        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diff)
            if needed <= k:
                right = mid
            else:
                left = mid + 1
        target = left
        remaining = k
        for i in range(len(diff)):
            reduction = max(0, diff[i] - target)
            diff[i] -= reduction
            remaining -= reduction
        for i in range(len(diff)):
            if remaining > 0 and diff[i] == target:
                diff[i] -= 1
                remaining -= 1
        return sum(d * d for d in diff)
