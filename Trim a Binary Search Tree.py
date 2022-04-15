# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root, low, high):
        def dfs(node):
            if not node: return node
            if node.val > high:
                return dfs(node.left)
            elif node.val < low:
                return dfs(node.right)
            else:
                node.left  = dfs(node.left)
                node.right = dfs(node.right)
                return node

        return dfs(root)
