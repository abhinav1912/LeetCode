class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) < 3:
            return 0
        l,n = 0,len(nums)
        while l < len(nums)-1:
            diff = nums[l+1]-nums[l]
            r = l+1
            while r<n and nums[r]-nums[r-1] == diff:
                r += 1
            no = r-l
            ans += ((no+1)*no)//2 - (2*no) + 1
            l = r-1
        return ans
        
