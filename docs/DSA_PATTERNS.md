# 🧠 Data Structures & Algorithms Pattern Mastery

A curated, practical guide to the core algorithmic patterns used throughout technical interviews and competitive programming, illustrated with direct links to solutions within this repository.

---

## Pattern Overview

| Pattern | Mental Model | Typical Time | Typical Space | Canonical Problem in Repo |
|:---|:---|:---:|:---:|:---|
| **[Arrays & Hashing](#1-arrays--hashing)** | Direct lookups, frequency tables, prefix sums | $O(N)$ | $O(N)$ | [01_TwoSum.py](../Arrays-and-Hashing/01_TwoSum.py) |
| **[Two Pointers & Sliding Window](#2-two-pointers--sliding-window)** | Shrinking/expanding search boundaries | $O(N)$ | $O(1)$ | [11_ContainerWithMostWater.py](../Two-Pointers-and-Sliding-Window/11_ContainerWithMostWater.py) |
| **[Binary Search](#3-binary-search)** | Logarithmic halving of ordered spaces | $O(\log N)$ | $O(1)$ | [33_SearchInRotatedArray.py](../Binary-Search/33_SearchInRotatedArray.py) |
| **[Linked Lists](#4-linked-lists)** | Pointer manipulation, fast/slow traversal | $O(N)$ | $O(1)$ | [141_LinkedListCycle.py](../Linked-Lists/141_LinkedListCycle.py) |
| **[Stacks & Queues](#5-stacks--queues)** | LIFO matching, monotonic comparisons | $O(N)$ | $O(N)$ | [739_DailyTempereture.py](../Stacks-and-Queues/739_DailyTempereture.py) |
| **[Trees & BSTs](#6-trees--binary-search-trees)** | Recursive divide-and-conquer, ordering properties | $O(N)$ | $O(H)$ | [98_ValidateBinarySearchTree.py](../Trees-and-Binary-Search-Trees/98_ValidateBinarySearchTree.py) |
| **[Graphs](#7-graphs)** | BFS (shortest path) / DFS (reachability) / Union-Find | $O(V + E)$ | $O(V)$ | [200_NumberOfIsland.py](../Graphs/200_NumberOfIsland.py) |
| **[Heaps & Priority Queues](#8-heaps--priority-queues)** | Top-K elements, dynamic extrema | $O(N \log K)$ | $O(K)$ | [347_TopKFrequentElements.py](../Heaps-and-Priority-Queues/347_TopKFrequentElements.py) |
| **[Backtracking](#9-backtracking)** | State-space tree exploration with pruning | $O(K^N)$ | $O(N)$ | [46_Permutations.py](../Backtracking/46_Permutations.py) |
| **[Greedy Algorithms](#10-greedy-algorithms)** | Local optimal choice with no regrets | $O(N \log N)$ or $O(N)$ | $O(1)$ | [55_jumpGame.py](../Greedy-Algorithms/55_jumpGame.py) |
| **[Dynamic Programming](#11-dynamic-programming)** | Overlapping subproblems, optimal substructure | $O(N \cdot M)$ | $O(N)$ or $O(1)$ | [72_edit_distance.py](../Dynamic-Programming/72_edit_distance.py) |
| **[Intervals](#12-intervals)** | Sorting by start/end times, sweep line | $O(N \log N)$ | $O(N)$ | [56_MergeInterval.py](../Intervals/56_MergeInterval.py) |
| **[Math & Bit Manipulation](#13-math--bit-manipulation)** | Bitwise XOR/AND masking, number theory | $O(1)$ or $O(\log N)$ | $O(1)$ | [136_SingleNumber.py](../Math-and-Bit-Manipulation/136_SingleNumber.py) |

---

## 1. Arrays & Hashing

### When to Use
- You need $O(1)$ lookup for previously encountered items.
- You need to track frequencies, detect duplicates, or group items by key.
- Problems require precomputing cumulative information (Prefix Sums, Suffix Products).

### Key Repository Examples
- **Hash Map Pair Matching**: [01_TwoSum.py](../Arrays-and-Hashing/01_TwoSum.py)
- **Hash Table Grouping**: [49_GroupAnagrams.py](../Arrays-and-Hashing/49_GroupAnagrams.py)
- **Unordered Sequence Set Lookup**: [128_LongestConsicutiveSequences.py](../Arrays-and-Hashing/128_LongestConsicutiveSequences.py)
- **Prefix / Suffix Precomputation**: [238_ProductOfArrayExceptSelf.py](../Arrays-and-Hashing/238_ProductOfArrayExceptSelf.py)
- **Static Range Sums**: [303_RangeSumQuery.py](../Arrays-and-Hashing/303_RangeSumQuery.py)

---

## 2. Two Pointers & Sliding Window

### When to Use
- **Two Pointers**: Input is sorted (or sortable), or examining symmetric elements from ends toward center.
- **Sliding Window**: Contiguous subarrays or substrings meeting a dynamic or fixed condition (e.g., sum $\ge K$, at most $K$ distinct elements).

### Key Repository Examples
- **Shrinking Two Pointers**: [11_ContainerWithMostWater.py](../Two-Pointers-and-Sliding-Window/11_ContainerWithMostWater.py)
- **3Sum Variation**: [16_3Sum_Closest.py](../Two-Pointers-and-Sliding-Window/16_3Sum_Closest.py)
- **Dynamic Sliding Window**: [03_LongestsubstringWithoutRepeatingCharacter.py](../Two-Pointers-and-Sliding-Window/03_LongestsubstringWithoutRepeatingCharacter.py)
- **Hard Window Matching**: [76_minimumWindowSubstring.py](../Two-Pointers-and-Sliding-Window/76_minimumWindowSubstring.py)
- **In-place Partition (Dutch National Flag)**: [75_SortColors.py](../Two-Pointers-and-Sliding-Window/75_SortColors.py)

---

## 3. Binary Search

### When to Use
- Array is sorted or rotated.
- The answer space is monotonic (e.g., "Find minimum capacity such that...").
- Looking for target insertion or boundary indices.

### Key Repository Examples
- **Rotated Sorted Array**: [33_SearchInRotatedArray.py](../Binary-Search/33_SearchInRotatedArray.py)
- **Insertion Position**: [35_SearchInsertionPosition.py](../Binary-Search/35_SearchInsertionPosition.py)
- **Rotated Array Extrema**: [153_Find_Minimum_in_Rotated_Sorted_Array.py](../Binary-Search/153_Find_Minimum_in_Rotated_Sorted_Array.py)
- **Median of Two Sorted Arrays (C++)**: [04_MedianOfTwoSortedArray.cpp](../Binary-Search/04_MedianOfTwoSortedArray.cpp)

---

## 4. Linked Lists

### When to Use
- Sequential node relationships without random access.
- In-place reversals, interleaving, or cycle detection.
- Fast & slow pointer (Floyd’s Cycle Finding) technique.

### Key Repository Examples
- **Digit Addition with Carry**: [02_AddTwoNumbers.py](../Linked-Lists/02_AddTwoNumbers.py)
- **In-place Reversal**: [206_ReverseLinkedlist.py](../Linked-Lists/206_ReverseLinkedlist.py)
- **Cycle Detection**: [141_LinkedListCycle.py](../Linked-Lists/141_LinkedListCycle.py)
- **Palindrome Linked List**: [234_PalindromeList.py](../Linked-Lists/234_PalindromeList.py)
- **List Rotation**: [61_RotateList.py](../Linked-Lists/61_RotateList.py)

---

## 5. Stacks & Queues

### When to Use
- Matching nested pairs (parentheses, HTML tags).
- **Monotonic Stack**: Finding the next greater / next smaller element in $O(N)$ total time.
- Processing items in strict FIFO order (queues/deques for sliding windows or BFS).

### Key Repository Examples
- **Bracket Matching**: [20_ValidParanthesis.py](../Stacks-and-Queues/20_ValidParanthesis.py)
- **Next Greater Element**: [739_DailyTempereture.py](../Stacks-and-Queues/739_DailyTempereture.py)
- **Online Stream Evaluation**: [901_Online_Stock_Price.py](../Stacks-and-Queues/901_Online_Stock_Price.py)
- **String Parsing with Stack**: [394_decodeString.py](../Stacks-and-Queues/394_decodeString.py)
- **O(1) Min Stack**: [155_minStack.py](../Stacks-and-Queues/155_minStack.py)

---

## 6. Trees & Binary Search Trees

### When to Use
- Hierarchical data representation.
- In-order traversal yields sorted order (BST).
- Height, path sums, lowest common ancestors via recursion.

### Key Repository Examples
- **In-order Traversal**: [94_BinaryTreeInorderTraversal.py](../Trees-and-Binary-Search-Trees/94_BinaryTreeInorderTraversal.py)
- **BST Invariant Verification**: [98_ValidateBinarySearchTree.py](../Trees-and-Binary-Search-Trees/98_ValidateBinarySearchTree.py)
- **Depth Calculation**: [104_MaximumDepthOfBinaryTree.py](../Trees-and-Binary-Search-Trees/104_MaximumDepthOfBinaryTree.py)
- **Target Path Sum**: [112_PathSum.py](../Trees-and-Binary-Search-Trees/112_PathSum.py)
- **Prefix Tree (Trie)**: [208_ImplenentTrie.py](../Trees-and-Binary-Search-Trees/208_ImplenentTrie.py)

---

## 7. Graphs

### When to Use
- Modeling networks, dependencies, or grid navigation.
- **BFS**: Unweighted shortest paths, level-order expansion.
- **DFS**: Cycle detection, connected components, path finding.
- **Topological Sort**: Resolving prerequisite orders (DAGs).

### Key Repository Examples
- **Connected Components (Grid BFS/DFS)**: [200_NumberOfIsland.py](../Graphs/200_NumberOfIsland.py)
- **Graph Deep Copy**: [133_CloneGraph.py](../Graphs/133_CloneGraph.py)
- **Topological Sort / Prerequisite Cycle Detection**: [207_CourseSelection.py](../Graphs/207_CourseSelection.py) & [210_CourseScheduleII.py](../Graphs/210_CourseScheduleII.py)
- **Shortest Path State Space (BFS)**: [752_openTheLock.py](../Graphs/752_openTheLock.py)
- **Multi-source BFS**: [2812_findTheSafestPathInAGrid.py](../Graphs/2812_findTheSafestPathInAGrid.py)

---

## 8. Heaps & Priority Queues

### When to Use
- Need continuous access to the smallest or largest element without full sorting.
- Keeping track of the Top-K elements in a stream.

### Key Repository Examples
- **Frequency Heap**: [347_TopKFrequentElements.py](../Heaps-and-Priority-Queues/347_TopKFrequentElements.py)
- **Difference Optimization**: [2333_MinimumSumOfSquaredDifference.py](../Heaps-and-Priority-Queues/2333_MinimumSumOfSquaredDifference.py)

---

## 9. Backtracking

### When to Use
- Finding all combinations, permutations, subsets, or solving constraint satisfaction (Sudoku, N-Queens).
- Must explore all possible candidates and backtrack upon reaching an invalid state.

### Key Repository Examples
- **Balanced Bracket Generation**: [22_Generate_Parantheses.py](../Backtracking/22_Generate_Parantheses.py)
- **Permutations**: [46_Permutations.py](../Backtracking/46_Permutations.py)
- **Systematic Pruning**: [301_RemoveInvalidParantheses.py](../Backtracking/301_RemoveInvalidParantheses.py)

---

## 10. Greedy Algorithms

### When to Use
- A globally optimal solution can always be reached by choosing a locally optimal step.
- Optimal substructure with the greedy choice property (no reconsidering past decisions).

### Key Repository Examples
- **Reachability Range**: [55_jumpGame.py](../Greedy-Algorithms/55_jumpGame.py)
- **Stock Single-Pass Valley/Peak**: [121_Best_Time_to_Buy_and_Sell_Stock.py](../Greedy-Algorithms/121_Best_Time_to_Buy_and_Sell_Stock.py)
- **Simulation**: [860_lemonade_change.py](../Greedy-Algorithms/860_lemonade_change.py)
- **Forward-Backward Height Bounding**: [1840_maximumBuildingHeight.py](../Greedy-Algorithms/1840_maximumBuildingHeight.py)

---

## 11. Dynamic Programming

### When to Use
- Overlapping subproblems + optimal substructure.
- Choices made at step $i$ depend on optimal solutions to smaller sub-states.
- Optimization problems asking for maximum, minimum, or total number of ways.

### Key Repository Examples
- **1D State Transitions**: [70_ClimbingStairs.py](../Dynamic-Programming/70_ClimbingStairs.py)
- **2D String Transformation**: [72_edit_distance.py](../Dynamic-Programming/72_edit_distance.py)
- **Substring DP**: [5_Longest_Palindromic_Substring.py](../Dynamic-Programming/5_Longest_Palindromic_Substring.py)
- **Decision State Machines**: [188_Best_Time_to_Buy_and_Sell_Stock_lV.py](../Dynamic-Programming/188_Best_Time_to_Buy_and_Sell_Stock_lV.py)
- **Grid DP with State Validation**: [2267_CheckIfThreeIsAValidParanthesis.py](../Dynamic-Programming/2267_CheckIfThreeIsAValidParanthesis.py)

---

## 12. Intervals

### When to Use
- Events with start and end times, overlapping resource allocation, scheduling.
- Techniques: Sort by start time, difference arrays (prefix sweep), or min-heap for active intervals.

### Key Repository Examples
- **Interval Merging**: [56_MergeInterval.py](../Intervals/56_MergeInterval.py)
- **Booking Conflict Detection**: [729_MyCalender1.py](../Intervals/729_MyCalender1.py)
- **Difference Array / Sweep Line**: [1094_CarPooling.py](../Intervals/1094_CarPooling.py) & [1109_CorporateFlightBooking.py](../Intervals/1109_CorporateFlightBooking.py)

---

## 13. Math & Bit Manipulation

### When to Use
- In-place flags, bitwise masks, parity checks, power of two checks (`n & (n - 1) == 0`).
- Number theory (primes, GCD/LCM, modular arithmetic).

### Key Repository Examples
- **XOR Cancellation**: [136_SingleNumber.py](../Math-and-Bit-Manipulation/136_SingleNumber.py)
- **Hamming Weight (Bit Counting)**: [191_NumberOf1Bits.py](../Math-and-Bit-Manipulation/191_NumberOf1Bits.py)
- **Sieve of Eratosthenes**: [204_CountPrimes.py](../Math-and-Bit-Manipulation/204_CountPrimes.py)
- **Bitwise Power of Two**: [231_PowerOfTwo.py](../Math-and-Bit-Manipulation/231_PowerOfTwo.py)

