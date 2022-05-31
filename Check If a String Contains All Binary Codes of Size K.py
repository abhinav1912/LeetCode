class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = {i:0 for i in range(1<<k)}
        mask = (1<<k)-1
        c = 0
        if len(s) < k:
            return False
        for i in range(k):
            c = c<<1 | int(s[i]!="0")
        d[c] = 1
        for i in range(k, len(s)):
            c = c<<1 | int(s[i]!="0")
            c &= mask
            d[c] = 1
        if 0 in d.values():
            return False
        return True
