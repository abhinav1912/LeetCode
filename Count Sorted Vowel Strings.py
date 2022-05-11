class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1,1,1,1,1]
        for i in range(2,n+1):
            temp = [0,0,0,0,0]
            for j in range(4,-1,-1):
                for k in range(j, -1, -1):
                    temp[k] += dp[j]
            dp = temp
        return sum(dp)
