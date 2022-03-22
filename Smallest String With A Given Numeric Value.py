class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        l = [1 for i in range(n)]
        s = k-sum(l)
        r = n-1
        while s:
            temp = min(s, 25)
            s -= temp
            l[r] += temp
            r -= 1
        return ''.join(chr(x + ord('a') - 1) for x in l)
