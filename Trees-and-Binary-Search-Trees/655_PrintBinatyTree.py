class Solution:
    def printTree(self, root):
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        h = get_height(root)
        rows = h
        cols = 2 ** h - 1

        ans = [[""] * cols for _ in range(rows)]

        def dfs(node, r, left, right):
            if not node:
                return

            mid = (left + right) // 2
            ans[r][mid] = str(node.val)

            dfs(node.left, r + 1, left, mid - 1)
            dfs(node.right, r + 1, mid + 1, right)

        dfs(root, 0, 0, cols - 1)

        return ans