class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l,r = max(nums), sum(nums)
        ans = r+1
        while l<=r:
            mid = (l+r)//2
            curr = 0
            x = m
            for i in nums:
                curr += i
                if curr > mid:
                    x -= 1
                    curr = i
            if x <= 0:
                l = mid+1
            else:
                ans = mid
                r = mid-1
        return ans
