'''
3700. Number of ZigZag Arrays II
Hard
Topics
premium lock icon
Companies
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 

Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

​​​​​​​There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.

 

Constraints:

3 <= n <= 109
1 <= l < r <= 75​​​​​​​
 
Accepted
37,849/59.6K

'''
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        sz = 2 * m

        T = [[0] * sz for _ in range(sz)]

        for i in range(m):
            for j in range(i):
                T[i][m + j] = 1

        for i in range(m):
            for j in range(i + 1, m):
                T[m + i][j] = 1

        def mat_mul(A, B):
            C = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                for k in range(sz):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(sz):
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(M, e):
            R = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                R[i][i] = 1

            while e:
                if e & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                e >>= 1
            return R

        def mat_vec_mul(M, v):
            res = [0] * sz
            for i in range(sz):
                s = 0
                row = M[i]
                for j in range(sz):
                    s = (s + row[j] * v[j]) % MOD
                res[i] = s
            return res

        init = [0] * sz

        for i in range(m):
            init[i] = i
            init[m + i] = m - 1 - i

        P = mat_pow(T, n - 2)
        ans = mat_vec_mul(P, init)

        return sum(ans) % MOD
