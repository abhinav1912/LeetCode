from collections import defaultdict, Counter
class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.stack = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        newFreq = self.freq[val]
        self.stack[newFreq].append(val)
        self.maxFreq = max(newFreq, self.maxFreq)
        

    def pop(self) -> int:
        x = self.stack[self.maxFreq].pop()
        self.freq[x] -= 1
        if not self.stack[self.maxFreq]:
            self.maxFreq -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
