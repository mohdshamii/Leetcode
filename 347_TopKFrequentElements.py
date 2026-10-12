from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mp = Counter(nums)
        return [x for x, freq in mp.most_common(k)]
