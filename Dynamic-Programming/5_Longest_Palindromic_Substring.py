'''

5. Longest Palindromic Substring


Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        longest = ""
        for i in range(len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i + 1)
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest
