class MyHashSet:

    def __init__(self):
        self.s = set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        self.s.discard(key)
        # if key in self.s:
        #     self.s.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.s
