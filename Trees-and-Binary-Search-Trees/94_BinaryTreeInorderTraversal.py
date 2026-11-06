class Solution:
    def inorderTraversal(self, root):
        ans = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)       # Left
            ans.append(node.val) # Root
            dfs(node.right)      # Right

        dfs(root)
        return ans
