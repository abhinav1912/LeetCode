from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i,c in enumerate(s)}
        visit = set()
        stack = ["!"]
        for i, c in enumerate(s):
            if c in visit:
                continue
            while c < stack[-1] and last[stack[-1]] > i:
                visit.remove(stack.pop())
            
            visit.add(c)
            stack.append(c)
        return ''.join(stack[1:])
