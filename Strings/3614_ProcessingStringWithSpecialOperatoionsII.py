'''
3614. Process String with Special Operations II

You are given a string s consisting of lowercase English letters and the special characters: '*', '#', and '%'.

You are also given an integer k.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the kth character of the final string result. If k is out of the bounds of result, return '.'.

 

Example 1:

Input: s = "a#b%*", k = 1

Output: "a"

Explanation:

i	s[i]	Operation	Current result
0	'a'	Append 'a'	"a"
1	'#'	Duplicate result	"aa"
2	'b'	Append 'b'	"aab"
3	'%'	Reverse result	"baa"
4	'*'	Remove the last character	"ba"
The final result is "ba". The character at index k = 1 is 'a'.

Example 2:

Input: s = "cd%#*#", k = 3

Output: "d"

Explanation:

i	s[i]	Operation	Current result
0	'c'	Append 'c'	"c"
1	'd'	Append 'd'	"cd"
2	'%'	Reverse result	"dc"
3	'#'	Duplicate result	"dcdc"
4	'*'	Remove the last character	"dcd"
5	'#'	Duplicate result	"dcddcd"
The final result is "dcddcd". The character at index k = 3 is 'd'.

Example 3:

Input: s = "z*#", k = 0

Output: "."

Explanation:

i	s[i]	Operation	Current result
0	'z'	Append 'z'	"z"
1	'*'	Remove the last character	""
2	'#'	Duplicate the string	""
The final result is "". Since index k = 0 is out of bounds, the output is '.'.

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters and special characters '*', '#', and '%'.
0 <= k <= 1015
The length of result after processing s will not exceed 1015.
'''
class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        length = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = length[i]

            if 'a' <= ch <= 'z':
                length[i + 1] = cur + 1
            elif ch == '*':
                length[i + 1] = max(0, cur - 1)
            elif ch == '#':
                length[i + 1] = cur * 2
            else:  # '%'
                length[i + 1] = cur

        if k >= length[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            L = length[i]

            if 'a' <= ch <= 'z':
                if k == L:
                    return ch

            elif ch == '#':
                if k >= L:
                    k -= L

            elif ch == '%':
                k = L - 1 - k

            # '*' => k unchanged

        return '.'
