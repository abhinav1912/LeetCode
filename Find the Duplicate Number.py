class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bit = 0
        for i in nums:
            x = 1 << i
            if bit & x:
                return i
            bit |= x
