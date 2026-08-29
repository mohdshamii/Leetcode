from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Courses with no prerequisites
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        return completed == numCourses
