class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count('W')
        ans = white

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white += 1

            if blocks[i - k] == 'W':
                white -= 1

            ans = min(ans, white)

        return ans
