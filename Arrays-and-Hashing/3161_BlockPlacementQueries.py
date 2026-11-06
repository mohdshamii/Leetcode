'''
3161. Block Placement Queries

There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

 

Example 1:

Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

Output: [false,true,true]

Explanation:



For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:

Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

Output: [true,true,false]

Explanation:



Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.
 

Constraints:

1 <= queries.length <= 15 * 104
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 104, 3 * queries.length)
The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
The input is generated such that there is at least one query of type 2.
 

'''
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class Solution:
    def getResults(self, queries):
        mx = max(q[1] for q in queries)

        obstacles = set()
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        sl = SortedList([0, mx])
        for x in obstacles:
            sl.add(x)

        bit = FenwickMax(mx + 1)

        arr = list(sl)
        for i in range(1, len(arr)):
            bit.update(arr[i], arr[i] - arr[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 2:
                _, x, sz = q

                idx = sl.bisect_right(x) - 1
                pre = sl[idx]

                best = max(bit.query(pre), x - pre)
                ans.append(best >= sz)

            else:
                x = q[1]

                idx = sl.bisect_left(x)
                prev_ob = sl[idx - 1]
                next_ob = sl[idx + 1]

                sl.remove(x)

                # merged gap after removing x
                bit.update(next_ob, next_ob - prev_ob)

        return ans[::-1]
