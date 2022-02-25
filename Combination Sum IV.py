class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        nums.sort()
        for i in nums:
            if i <= target:
                dp[i] = 1
            else:
                break
        for i in range(target+1):
            for j in nums:
                if i-j>0:
                    dp[i] += dp[i-j]
                else:
                    break
        return dp[target]
