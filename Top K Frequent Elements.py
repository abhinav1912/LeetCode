from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        for i in nums:
            c[i] += 1
        l = sorted([[c[item], item] for item in c], reverse=True)[:k]
        return [i[1] for i in l]
