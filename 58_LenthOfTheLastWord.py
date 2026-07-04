class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        p = len(s) - 1

        # Skip trailing spaces
        while p >= 0 and s[p] == " ":
            p -= 1

        # Count last word
        while p >= 0 and s[p] != " ":
            count += 1
            p -= 1

        return count
