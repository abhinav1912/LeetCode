class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        l = [poured]
        for i in range(query_row):
            l_new = [0]*(len(l)+1)
            for j in range(len(l)):
                pour = (l[j]-1)/2
                if pour > 0:
                    l_new[j] += pour
                    l_new[j+1] += pour
            l = l_new
        return min(1,l[query_glass])
