class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = 10001
        l = [0]*(n)
        for i in nums:
            l[i] += 1
        l[-1] = l[-1]*(n-1)
        l[-2] = l[-2]*(n-2)
        l[-3] = l[-3]*(n-3)
        for i in range(n-4,-1,-1):
            l[i] = (l[i]*i) + max(l[i+2], l[i+3])
        return max(l[0], l[1])
