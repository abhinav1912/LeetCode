class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            jump = max(jump, nums[i]+i)
            if jump >= len(nums)-1:
                return True
            if i>=jump:
                return False
        return False
