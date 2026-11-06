'''
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:
'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        ans = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += len(s) - right
                count[s[left]] -= 1
                left += 1

        return ans
