class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        i = 0
        def parse():
            nonlocal i
            res = {""}
            cur = set()
            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    cur |= res
                    res = {""}
                    i += 1
                else:
                    if expression[i] == '{':
                        i += 1
                        temp = parse()
                        i += 1
                    else:
                        temp = {expression[i]}
                        i += 1
                    new_res = set()
                    for a in res:
                        for b in temp:
                            new_res.add(a + b)
                    res = new_res
            cur |= res
            return cur
        return sorted(parse())
