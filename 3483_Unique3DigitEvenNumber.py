class Solution:
    def totalNumbers(self, digits):
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if digits[i] != 0 and digits[k] % 2 == 0:
                        ans.add(num)
        return len(ans
