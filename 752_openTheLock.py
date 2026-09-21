from collections import deque
class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        q = deque([("0000", 0)])
        seen = {"0000"}
        while q:
            state, steps = q.popleft()
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    nd = (digit + move) % 10
                    nxt = state[:i] + str(nd) + state[i+1:]
                    if nxt == target:
                        return steps + 1
                    if nxt not in dead and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
        return -1
