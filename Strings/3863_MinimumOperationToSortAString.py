class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i+1] for i in range(n-1)):
            return 0
        
        if n == 2:
            return -1
        
        counts = Counter(s)
        minCh, maxCh = min(s), max(s)
        if s[0] == minCh or s[-1] == maxCh:
            return 1
        elif s[0] == maxCh and s[-1] == minCh and counts[minCh] == 1 and counts[maxCh] == 1:
            return 3
        return 2
