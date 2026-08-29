class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        clones = {}
        def dfs(curr):
            if curr in clones:
                return clones[curr]
            copy = Node(curr.val)
            clones[curr] = cope
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
