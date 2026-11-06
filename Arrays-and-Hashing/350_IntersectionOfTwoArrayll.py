class Solution:
    def intersect(self, nums1, nums2):
        ans = []

        for x in nums1:
            if x in nums2:
                ans.append(x)
                nums2.remove(x)

        return ans
