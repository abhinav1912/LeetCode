class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        c = [(i.count("0"),i.count("1")) for i in strs]
        mx = -float("inf")
        
        @lru_cache(None)
        def dfs(mm, nn, i):
            if mm < 0 or nn < 0:
                return mx
            if i == len(strs):
                return 0
            z,o = c[i]
            return max(1+dfs(mm-z, nn-o,i+1), dfs(mm, nn, i+1))
        return dfs(m,n,0)
