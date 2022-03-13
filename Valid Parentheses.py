class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if d[t] != i:
                    return False
        
        if stack:
            return False
        return True
