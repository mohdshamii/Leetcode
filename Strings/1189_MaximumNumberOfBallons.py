'''
1189. Maximum Number of Balloons
Easy
Topics
premium lock icon
Companies
Hint
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
 

Note: This question is the same as 2287: Rearrange Characters to Make Target String.
'''
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)

        return min(
            cnt['b'],
            cnt['a'],
            cnt['l'] // 2,
            cnt['o'] // 2,
            cnt['n']
        )
