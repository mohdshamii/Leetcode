
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        longest = 0
        for x in seen:
            if x - 1 not in seen:
                current = x
                length = 1
                while current + 1 in seen:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
