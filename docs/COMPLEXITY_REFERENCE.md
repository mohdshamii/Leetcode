# ⏱️ Time & Space Complexity Reference

An essential computational complexity guide for technical interviews, LeetCode optimization, and algorithm design.

---

## 1. Big-O Complexity Hierarchy

From most efficient to least efficient as input size $N$ grows:

```
O(1) < O(log N) < O(√N) < O(N) < O(N log N) < O(N²) < O(N³) < O(2^N) < O(N!)
```

| Notation | Common Name | Typical Algorithms / Operations |
|:---|:---|:---|
| **$O(1)$** | Constant | Hash map get/put, array index lookup, stack push/pop, bitwise operations |
| **$O(\log N)$** | Logarithmic | Binary search, balanced BST operations, Euclidean GCD, modular exponentiation |
| **$O(\sqrt{N})$** | Square Root | Primality test, integer factorization |
| **$O(N)$** | Linear | Single pass array traversal, two pointers, sliding window, counting sort |
| **$O(N \log N)$** | Linearithmic | Merge sort, heap sort, quick sort (average), sorting before two pointers |
| **$O(N^2)$** | Quadratic | Nested loops, bubble sort, pairwise comparisons, dynamic programming over 2D grids |
| **$O(N^3)$** | Cubic | Floyd-Warshall, matrix multiplication (standard) |
| **$O(2^N)$** | Exponential | Generating all subsets, recursive Fibonacci, unrestricted backtracking |
| **$O(N!)$** | Factorial | Generating all permutations, traveling salesperson problem (brute force) |

---

## 2. LeetCode Constraints Translation Rule

In competitive programming and technical interviews, platforms typically permit $\sim 10^7$ to $10^8$ basic operations per second (Python is often $\sim 10^6 - 10^7$, C++ is $\sim 10^8$). Use problem input constraints to deduce the target algorithmic complexity:

| Input Size ($N$) | Expected Time Complexity | Typical Algorithms |
|:---|:---|:---|
| **$N \le 10$ to $12$** | $O(N!)$ or $O(N^2 \cdot 2^N)$ | Generating permutations, Traveling Salesperson DP with bitmask |
| **$N \le 20$ to $25$** | $O(2^N)$ | Subset generation, recursion with backtracking, Meet in the Middle ($2^{N/2}$) |
| **$N \le 100$** | $O(N^4)$ or $O(N^3)$ | All-pairs shortest path (Floyd-Warshall), 3D dynamic programming |
| **$N \le 1{,}000$ to $2{,}000$** | $O(N^2)$ | 2D dynamic programming, nested loops, graph adjacency matrix algorithms |
| **$N \le 10^5$ to $2 \cdot 10^5$** | $O(N \log N)$ or $O(N)$ | Sorting, Binary Search, Heaps, Trees, Monotonic Stacks, Segment Trees |
| **$N \ge 10^6$ to $10^9$** | $O(\log N)$ or $O(1)$ | Pure Binary Search, Math formulas, Bit Manipulation |

---

## 3. Auxiliary Space vs Total Space

- **Total Space**: Total memory allocated, including inputs and outputs.
- **Auxiliary Space**: Temporary or extra memory used by the algorithm excluding the inputs (and sometimes excluding the return value if required by the problem statement).

### Recursion Stack Space
Every recursive function call consumes a frame on the call stack proportional to recursion depth $H$:
- **Balanced Binary Tree**: Depth $H = O(\log N) \implies O(\log N)$ stack space.
- **Skewed Binary Tree / Degenerate List**: Depth $H = O(N) \implies O(N)$ stack space.
- **Python Note**: Default Python recursion limit is typically $1{,}000$. Deep recursions ($N > 1000$) require `sys.setrecursionlimit(...)` or rewriting iteratively using an explicit `list` as a stack.

---

## 4. Complexity Patterns by Data Structure

| Data Structure | Access | Search | Insertion | Deletion | Space |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Array** | $O(1)$ | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Stack / Queue** | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ |
| **Singly Linked List** | $O(N)$ | $O(N)$ | $O(1)^*$ | $O(1)^*$ | $O(N)$ |
| **Hash Table** | N/A | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | $O(N)$ |
| **Binary Search Tree** | $O(\log N)$ avg | $O(\log N)$ avg | $O(\log N)$ avg | $O(\log N)$ avg | $O(N)$ |
| **Binary Heap** | N/A | $O(N)$ | $O(\log N)$ | $O(\log N)$ | $O(N)$ |
| **Trie** | N/A | $O(L)$ | $O(L)$ | $O(L)$ | $O(\Sigma \cdot L \cdot N)$ |

*\* Insertion/deletion in linked lists is $O(1)$ once the target node pointer is already identified.*

