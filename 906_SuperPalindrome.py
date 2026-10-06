class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)
        def is_palindrome(n):
            s = str(n)
            return s == s[::-1]
        ans = 0
        for half in range(1, 100000):
            s = str(half)
            root = int(s + s[-2::-1])
            if root * root > R:
                break
            square = root * root
            if square >= L and is_palindrome(square):
                ans += 1
            root = int(s + s[::-1])
            if root * root <= R:
                square = root * root
                if square >= L and is_palindrome(square):
                    ans += 1
        return ans
