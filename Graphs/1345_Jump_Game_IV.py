'''
1345. Jump Game IV

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
'''
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        mp = defaultdict(list)
        for i, val in enumerate(arr):
            mp[val].append(i)
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0
        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                if idx == n - 1:
                    return steps
                if idx - 1 >= 0 and not visited[idx - 1]:
                    visited[idx - 1] = True
                    q.append(idx - 1)
                if idx + 1 < n and not visited[idx + 1]:
                    visited[idx + 1] = True
                    q.append(idx + 1)
                for next_idx in mp[arr[idx]]:
                    if not visited[next_idx]:
                        visited[next_idx] = True
                        q.append(next_idx)
                mp[arr[idx]].clear()
            steps += 1
        return -1
