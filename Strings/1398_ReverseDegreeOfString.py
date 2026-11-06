class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s, 1):
            ans += (26 - (ord(c) - ord('a'))) * i
        return ans
