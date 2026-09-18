class Solution:
    def maxNumOfSubstrings(self, s: str):
        first = [len(s)] * 26
        last = [-1] * 26
        for i, c in enumerate(s):
            x = ord(c) - 97
            first[x] = min(first[x], i)
            last[x] = i
        a = []
        for x in range(26):
            if last[x] == -1:
                continue
            l, r = first[x], last[x]
            i = l
            while i <= r:
                y = ord(s[i]) - 97
                if first[y] < l:
                    break
                r = max(r, last[y])
                i += 1
            else:
                a.append((r, l))
        a.sort()
        ans = []
        end = -1
        for r, l in a:
            if l > end:
                ans.append(s[l:r + 1])
                end = r
        return ans
