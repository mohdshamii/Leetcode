from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k
        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, server = heapq.heappop(busy)
                available.add(server)
            if not available:
                continue
            idx = i % k
            pos = available.bisect_left(idx)
            if pos == len(available):
                pos = 0
            server = available.pop(pos)
            count[server] += 1
            heapq.heappush(busy, (a + l, server))
        max_count = max(count)
        return [i for i, c in enumerate(count) if c == max_count]