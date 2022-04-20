# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.push(root)
    
    def push(self, root):
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        node = self.st.pop()
        self.push(node.right)
        return node.val

    def hasNext(self) -> bool:
        return (len(self.st) > 0)
