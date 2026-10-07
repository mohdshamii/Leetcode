class Solution:
    def removeInvalidParentheses(self, s: str):
        res = set()
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
        def backtrack(i, path, balance, lrem, rrem):
            if i == len(s):
                if balance == 0 and lrem == 0 and rrem == 0:
                    res.add("".join(path))
                return
            ch = s[i]
            if ch == '(' and lrem > 0:
                backtrack(i + 1, path, balance, lrem - 1, rrem)
            elif ch == ')' and rrem > 0:
                backtrack(i + 1, path, balance, lrem, rrem - 1)
            if ch != '(' and ch != ')':
                path.append(ch)
                backtrack(i + 1, path, balance, lrem, rrem)
                path.pop()
            elif ch == '(':
                path.append(ch)
                backtrack(i + 1, path, balance + 1, lrem, rrem)
                path.pop()
            else:  
                if balance > 0:
                    path.append(ch)
                    backtrack(i + 1, path, balance - 1, lrem, rrem)
                    path.pop()
        backtrack(0, [], 0, left_rem, right_rem)
        return list(res)
