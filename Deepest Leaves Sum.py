from collections import Counter
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.d = Counter()
        self.dfs(root, 0)
        return self.d[max(self.d.keys())]
    def dfs(self, root, depth):
        if not root:
            return
        self.d[depth] += root.val
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)
