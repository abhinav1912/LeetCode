class Solution:
    def countBits(self, n: int) -> List[int]:
        p = 1
        ans = [0]*(n+1)
        if n:
            ans[1] = 1
        for i in range(2, n+1):
            if i == (p<<1):
                ans[i] = 1
                p = p<<1
            else:
                ans[i] = 1 + ans[i-p]
        return ans
