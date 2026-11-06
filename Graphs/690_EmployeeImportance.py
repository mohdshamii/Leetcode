"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id):
        d={e.id:e for e in employees}
        def dfs(i):
            e=d[i]
            return e.importance+sum(dfs(x) for x in e.subordinates)
        return dfs(id)
