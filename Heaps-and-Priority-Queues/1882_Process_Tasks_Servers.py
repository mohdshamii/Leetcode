'''
1882. Process Tasks Using Servers
Medium
Topics
premium lock icon
Companies
Hint
You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

Return the array ans​​​​.

 

Example 1:

Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
Example 2:

Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]
Explanation: Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.
 

Constraints:

servers.length == n
tasks.length == m
1 <= n, m <= 2 * 105
1 <= servers[i], tasks[j] <= 2 * 105
'''
import heapq #import heapq for priority queue operations
class Solution: #Define the Solution class
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]: #Define the assignTasks method that takes two lists of integers as input and returns a list of integers
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers) #Create a min-heap of free servers based on their weights and indices
        busy_servers = [] #Create an empty list to keep track of busy servers
        ans = [] #Create an empty list to store the indices of servers assigned to tasks
        time = 0 #Initialize the time variable to keep track of the current time
        for i, task in enumerate(tasks): #Iterate through the tasks and their indices
            time = max(time, i) #Update the current time to be the maximum of the current time and the index of the task
            while busy_servers and busy_servers[0][0] <= time: #While there are busy servers and the earliest busy server is free at or before the current time
                _, weight, index = heapq.heappop(busy_servers) #Pop the earliest busy server from the busy_servers heap
                heapq.heappush(free_servers, (weight, index)) #Push the freed server back into the free_servers heap
            if free_servers: #If there are free servers available
                weight, index = heapq.heappop(free_servers) #Pop the server with the smallest weight (and index in case of a tie) from the free_servers heap
                ans.append(index) #Append the index of the assigned server to the ans list
                heapq.heappush(busy_servers, (time + task, weight, index)) #Push the assigned server into the busy_servers heap with the time it will be free again
            else:
                time = busy_servers[0][0] #If there are no free servers, update the current time to the time when the earliest busy server will be free
                while busy_servers and busy_servers[0][0] <= time: #While there are busy servers and the earliest busy server is free at or before the updated time
                    _, weight, index = heapq.heappop(busy_servers) #Pop the earliest busy server from the busy_servers heap
                    heapq.heappush(free_servers, (weight, index)) #Push the freed server back into the free_servers heap
                weight, index = heapq.heappop(free_servers) #Pop the server with the smallest weight (and index in case of a tie) from the free_servers heap
                ans.append(index) #Append the index of the assigned server to the ans list
                heapq.heappush(busy_servers, (time + task, weight, index)) #Push the assigned server into the busy_servers heap with the time it will be free again
        return ans  