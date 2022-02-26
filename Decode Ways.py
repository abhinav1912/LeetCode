class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[-1] = 1
        dp[-2] = int(s[-1]!="0")
        for i in range(n-2, -1, -1):
            if s[i]!="0":
                dp[i] += dp[i+1]
                c = int(s[i:i+2])
                if 1 <= c <= 26:
                    dp[i] += dp[i+2]
        return dp[0]
