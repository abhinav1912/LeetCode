class Solution:
    def search(self, nums: List[int], x: int) -> int:
        l, r = 0, len(nums)-1
        while (l<=r):
            mid = (l+r)//2
            if nums[mid]==x:
                return mid
            if nums[mid]>x:
                r = mid-1
            else:
                l = mid+1
        return -1
