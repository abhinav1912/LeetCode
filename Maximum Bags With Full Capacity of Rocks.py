class Solution:
    def maximumBags(self, c: List[int], r: List[int], a: int) -> int:
        n = len(c)
        ans = 0
        for i in range(n):
            c[i] -= r[i]
        c.sort()
        for i in range(n):
            a -= c[i]
            if a >= 0:
                ans += 1
            else:
                break
        return ans
