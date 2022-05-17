# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node, value):
            if not node:
                return None
            if node.val == value:
                return node
            return dfs(node.left, value) or dfs(node.right, value)
        return dfs(cloned, target.val)
