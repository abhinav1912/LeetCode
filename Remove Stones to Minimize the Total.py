from heapq import heapify, heappush, heappop
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-i for i in piles]
        heapify(h)
        for i in range(k):
            x = heappop(h)
            heappush(h, x//2)
        return -sum(h)
