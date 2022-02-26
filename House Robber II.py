class Solution:
    def rob_sub(self, nums: List[int]) -> int:
        rob, skip = 0,0
        for i in nums:
            rob, skip = i+skip, max(rob, skip)
        return max(rob, skip)

    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        return max(self.rob_sub(nums[:len(nums)-1]), self.rob_sub(nums[1:]))
