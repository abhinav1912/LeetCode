class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s = sorted([(sum(j), i) for i,j in enumerate(mat)])
        return [i[1] for i in s[:k]]
