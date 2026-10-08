class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0

        for c in s:
            if c == '(':
                depth += 1
                if depth > 1:
                    ans.append(c)

            else:
                depth -= 1
                if depth > 0:
                    ans.append(c)

        return ''.join(ans)
