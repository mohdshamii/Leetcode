class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        for left in range(upper, 10 ** (n - 1) - 1, -1):
            s = str(left)
            pal = int(s + s[::-1])
            x = upper
            while x * x >= pal:
                if pal % x == 0:
                    return pal % 1337
                x -= 1
        return 0
