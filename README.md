# LeetCode & DSA Tracker

A simple tracker for my LeetCode solutions, DSA practice, and revision progress.

## Progress at a Glance

| Metric | Current Progress |
|---|---:|
| Solution files | 228 |
| Unique problems | 218 |
| Python solutions | 208 |
| C++ solutions | 3 |
| SQL solutions | 10 |
| JavaScript solutions | 3 |
| Target | 1,000 problems |

> Update these numbers whenever the repository index is regenerated.

## Milestones

- [x] 50 problems
- [x] 100 problems
- [x] 200 problems
- [ ] 300 problems
- [ ] 500 problems
- [ ] 750 problems
- [ ] 1,000 problems

## Topic Tracker

| Topic | Solved | Done? |
|---|---:|:---:|
| Arrays and Hashing | 35 | [ ] |
| Backtracking | 4 | [ ] |
| Binary Search | 7 | [ ] |
| Database / SQL | 12 | [ ] |
| Dynamic Programming | 19 | [ ] |
| Graphs | 20 | [ ] |
| Greedy Algorithms | 17 | [ ] |
| Heaps and Priority Queues | 3 | [ ] |
| Intervals | 8 | [ ] |
| JavaScript | 3 | [ ] |
| Linked Lists | 6 | [ ] |
| Math and Bit Manipulation | 41 | [ ] |
| Shell | 1 | [ ] |
| Stacks and Queues | 18 | [ ] |
| Strings | 14 | [ ] |
| Trees and Binary Search Trees | 9 | [ ] |
| Two Pointers and Sliding Window | 12 | [ ] |

Topic counts can overlap with language-specific folders. Use the problem index for the full list.

## Daily Log

Add one short entry after each practice session.

| Date | Problems Solved | Main Topic | Revised? |
|---|---|---|---|
| YYYY-MM-DD | Problem IDs or count | Topic | Yes / No |
| YYYY-MM-DD | Problem IDs or count | Topic | Yes / No |

## Revision Tracker

Keep a short list of problems that need another attempt.

| Problem | Reason | Next Review | Done? |
|---|---|---|:---:|
| Problem ID / Name | Forgot pattern / TLE / Bug | YYYY-MM-DD | [ ] |

## Find Solutions

- **[Complete Problem Index](PROBLEM_INDEX.md)** — browse all solution files.
- **[DSA Patterns Guide](docs/DSA_PATTERNS.md)** — learn when to use each pattern.
- **[Complexity Reference](docs/COMPLEXITY_REFERENCE.md)** — time and space complexity.
- **[Interview Strategies](docs/INTERVIEW_STRATEGIES.md)** — problem-solving framework.
- **[Common Mistakes](docs/COMMON_MISTAKES.md)** — bugs and edge cases.
- **[Repository Verification](.github/workflows/verify.yml)** — automated checks.

## Repository Structure

Solutions are grouped by DSA pattern. Existing folders and files are kept in place.

```text
Leetcode/
├── Arrays-and-Hashing/
├── Backtracking/
├── Binary-Search/
├── Database/
├── Dynamic-Programming/
├── Graphs/
├── Greedy-Algorithms/
├── Heaps-and-Priority-Queues/
├── Intervals/
├── JavaScript/
├── Linked-Lists/
├── Math-and-Bit-Manipulation/
├── Shell/
├── Stacks-and-Queues/
├── Strings/
├── Trees-and-Binary-Search-Trees/
├── Two-Pointers-and-Sliding-Window/
├── docs/
├── scripts/
├── PROBLEM_INDEX.md
└── README.md
```

## Update the Tracker

Run this after adding new solutions:

```bash
python scripts/repo_tool.py all
```

Useful individual commands:

```bash
python scripts/repo_tool.py index
python scripts/repo_tool.py update-readme
python scripts/repo_tool.py validate
python scripts/repo_tool.py duplicates
python scripts/repo_tool.py check-links
```

## My Rule

**Solve → Save → Update index → Review mistakes → Repeat.**

Maintained by [mohdshamii](https://github.com/mohdshamii) · [LeetCode Profile](https://leetcode.com/mohdshamii)
