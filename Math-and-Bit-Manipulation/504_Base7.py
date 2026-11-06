class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        num = abs(num)
        ans = ""
        while num > 0:
            rem = num % 7
            ans += str(rem)
            num //= 7
        return sign + ans[::-1]
