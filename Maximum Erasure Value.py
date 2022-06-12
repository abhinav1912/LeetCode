from collections import Counter
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        c, s, ans = Counter(), 0, 0
        i,j,n = 0,0,len(nums)
        while j<n:
            if not c[nums[j]]:
                c[nums[j]] = 1
                s += nums[j]
                ans = max(s, ans)
            else:
                while i<j:
                    c[nums[i]] -= 1
                    s -= nums[i]
                    i += 1
                    if nums[i-1] == nums[j]:
                        s += nums[j]
                        c[nums[j]] = 1
                        break
            j += 1
        return ans
