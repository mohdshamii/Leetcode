# ⚠️ Common Algorithmic Mistakes & Gotchas

A catalog of frequent bugs, language quirks, and algorithmic traps encountered when solving LeetCode problems.

---

## 1. Algorithmic Gotchas

### Binary Search Boundary Errors
- **Midpoint calculation**:
  ```python
  # Safe against overflow in languages with fixed integer sizes (C++, Java)
  mid = low + (high - low) // 2
  ```
- **Loop condition vs pointer update**:
  - If using `while low <= high:`, use `low = mid + 1` and `high = mid - 1`.
  - If using `while low < high:`, ensure your branch either does `low = mid + 1` or `high = mid`, and check for potential infinite loops if `mid = (low + high) // 2` truncates towards `low`.

### Two Pointers & Sliding Window Termination
- **Off-by-One in Window Length**:
  - The number of elements between inclusive indices `left` and `right` is `right - left + 1`, **not** `right - left`.
- **Shrinking the Window Too Late**:
  - Ensure the window constraint (e.g., removing characters from frequency map) runs in a `while` loop, not an `if` statement, when multiple elements must be ejected.

### Graph BFS: Adding to `visited` at the Wrong Moment
- **Bug**: Adding a node to `visited` when it is popped from the queue.
  - Multiple neighbors can enqueue the exact same unvisited node, causing exponential queue explosions and TLE / Memory Limit Exceeded.
- **Fix**: Always mark nodes as `visited` immediately upon **pushing** to the queue.

### Dynamic Programming: 0-Index vs 1-Index Alignment
- In DP tables initialized with size `(n + 1) x (m + 1)` (e.g. Edit Distance or Knapsack), `dp[i][j]` maps to input string characters `s[i - 1]` and `t[j - 1]`. Mixing up `i` with `i - 1` leads to index out of bounds or corrupted state transitions.

---

## 2. Python Language Specific Traps

### 1. Slicing Creates an O(K) Memory Copy
```python
# MISTAKE: Checking prefix in loop using slicing creates a new string copy every iteration!
for i in range(len(s)):
    if s[i:i+len(sub)] == sub:  # O(len(sub)) time and memory allocation each step
        ...

# OPTIMIZED: Use pointers, startswith with start index, or rolling hash
if s.startswith(sub, i):
    ...
```

### 2. Mutable Default Arguments in Functions
```python
# DANGEROUS: Default list is shared across calls!
def backtrack(curr=[]):
    curr.append(1)

# CORRECT:
def backtrack(curr=None):
    if curr is None:
        curr = []
```

### 3. Shallow Copy vs Deep Copy When Storing Results
```python
# MISTAKE: Storing reference to mutable list in backtrack
result.append(path)      # All entries in result will mirror subsequent mutations!

# CORRECT: Store a snapshot copy
result.append(list(path))  # or path[:]
```

### 4. Integer Division with Negative Numbers
In Python:
`-3 // 2 == -2` (floors towards negative infinity), whereas in C++:
`-3 / 2 == -1` (truncates towards zero).
For truncation towards zero in Python, use `int(-3 / 2)`.

---

## 3. C++ Language Traps

### 1. `vector.size()` Unsigned Underflow
```cpp
// DANGEROUS: If nums is empty, nums.size() is 0u.
// 0u - 1 yields 18446744073709551615 (size_t max), causing infinite loop or segfault!
for (int i = 0; i < nums.size() - 1; ++i) { ... }

// CORRECT:
int n = nums.size();
for (int i = 0; i < n - 1; ++i) { ... }
```

### 2. Signed Integer Overflow in Sums
In C++, `int` is typically 32-bit (up to $\approx 2 \cdot 10^9$). When calculating midpoints or summing elements ($10^5 \times 10^5 = 10^{10}$), values exceed 32 bits and overflow:
```cpp
// Use long long for intermediate sums:
long long total = 0;
for (int x : nums) total += x;
```

