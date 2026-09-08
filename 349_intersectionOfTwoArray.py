class Solution:
    def intersection(self, nums1, nums2):
        ans = []

        for x in nums1:
            if x in nums2 and x not in ans:
                ans.append(x)

        return ans
