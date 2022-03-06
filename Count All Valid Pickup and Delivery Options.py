class Solution:
    def countOrders(self, n: int) -> int:
        if not n:
            return 1
        ans = 1
        while n:
            x = (2*n)-1
            ans = ((x*(x+1))//2 * ans)%1000000007
            n -= 1
        return ans
