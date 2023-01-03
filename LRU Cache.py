class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curr = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.map = {}

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.map[node.key]
    
    def add(self, node):
        node.next = self.tail
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        self.map[node.key] = node

    def get(self, key: int) -> int:
        x = self.map.get(key)
        if not x:
            return -1
        self.remove(x)
        self.add(x)
        return x.val

    def put(self, key: int, value: int) -> None:
        x = self.map.get(key)
        if x:
            self.remove(x)
        else:
            self.curr += 1
        if self.curr > self.cap:
            self.remove(self.head.next)
            self.curr -= 1
        n = Node(key, value)
        self.add(n)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
