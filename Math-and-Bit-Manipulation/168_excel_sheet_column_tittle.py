'''
168. Excel sheet column title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber:
            columnNumber -= 1
            res = chr(columnNumber % 26 + ord('A')) + res
            columnNumber //= 26

        return res
