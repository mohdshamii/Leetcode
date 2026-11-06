'''
60. Permutation Sequence
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 '''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math

        numbers = [str(i) for i in range(1, n + 1)]
        result = []

        k -= 1  

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)

            index = k // fact
            result.append(numbers[index])

            numbers.pop(index)

            k %= fact

        return "".join(result)
