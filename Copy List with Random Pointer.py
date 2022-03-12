"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map = {}
        curr = head
        while curr:
            map[curr] = Node(curr.val, curr.next, None)
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                map[curr].random = map[curr.random]
            if curr.next:
                map[curr].next = map[curr.next]
            curr = curr.next
        return map[head]
