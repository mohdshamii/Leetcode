class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0

            total = a + b + carry
            ans.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return ''.join(ans[::-1])
