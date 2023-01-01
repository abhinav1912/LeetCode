"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        a = Node(1, None, None, None)
        ans = a
        s, q2 = [head], []
        while (s or q2):
            if not s:
                s.append(q2.pop())
            curr = s.pop()
            if not curr:
                continue
            s.append(curr.child)
            q2.append(curr.next)
            curr.child, curr.next = None, None
            curr.prev = a
            a.next = curr
            a = a.next
        ans.next.prev = None
        return ans.next
