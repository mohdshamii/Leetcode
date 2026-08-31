class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        def dfs(node):
            visited[node] = True
            for nei in range(n):
                if isConnected[node][nei] == 1 and not visited[nei]:
                    dfs(nei)
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        return provinces
