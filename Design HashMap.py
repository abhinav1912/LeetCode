class MyHashMap:

    def __init__(self):
        self.s = {}

    def put(self, key: int, value: int) -> None:
        self.s[key] = value
        

    def get(self, key: int) -> int:
        if key not in self.s:
            return -1
        return self.s[key]

    def remove(self, key: int) -> None:
        self.s.pop(key, None)
