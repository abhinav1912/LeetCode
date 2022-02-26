class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if i+3<len(nums):
                dp[i] = max(dp[i+2], dp[i+3])
            elif i+2<len(nums):
                dp[i] = dp[i+2]
            dp[i] += nums[i]
        return max(dp)
