from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total < desiredTotal:
            return False
        @lru_cache(None)
        def dfs(mask, remaining):
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if mask & bit:
                    continue
                if i >= remaining or not dfs(mask | bit, remaining - i):
                    return True
            return False
        return dfs(0, desiredTotal)
