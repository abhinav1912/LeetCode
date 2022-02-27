# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        ans = 0
        while queue:
            count = len(queue)
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            while count:
                curr, width = queue.popleft()
                count -= 1
                if curr.left:
                    queue.append((curr.left, width*2))
                if curr.right:
                    queue.append((curr.right, (width*2)+1))
        return ans
