from collections import Counter
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        count = Counter()
        for i in nums:
            count[i] += 1
        j = 0
        for i in count.keys():
            if i%2==0:
                for k in range(count[i]):
                    nums[j] = i
                    j += 1
        for i in count.keys():
            if i%2==1:
                for k in range(count[i]):
                    nums[j] = i
                    j += 1
        return nums
