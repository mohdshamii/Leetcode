class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        right = 0

        for c in s:
            if c == '(':
                if right % 2 == 1:
                    ans += 1
                    right -= 1

                right += 2

            else:
                right -= 1

                if right < 0:
                    ans += 1
                    right += 2

        return ans + right
