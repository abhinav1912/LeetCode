# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root, temp):
            if not root:
                return 0
            right = dfs(root.right, temp)
            val = root.val
            root.val += right + temp
            left = dfs(root.left, right+val+temp)
            return val + left + right
        dfs(root, 0)
        return root
