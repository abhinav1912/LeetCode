# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = self.getNumbers(root)
        # print(nums)
        s = sum(int(i) for i in nums)
        return s
    
    def getNumbers(self, root):
        ans = []
        if root.left:
            ans += [str(root.val)+i for i in self.getNumbers(root.left)]
        if root.right:
            ans += [str(root.val)+i for i in self.getNumbers(root.right)]
        if not ans:
            ans.append(str(root.val))
        return ans
