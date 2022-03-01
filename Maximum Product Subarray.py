class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx,curr,mn = 1,0,1
        ans = -11
        for i in nums:
            curr = i
            l = sorted([mx*i, curr, mn*i])
            mx, mn = l[-1], l[0]
            ans = max(ans, mx)
        return ans
