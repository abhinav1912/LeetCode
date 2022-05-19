from collections import Counter
class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        def dfs(i,j):
            if dp[(i,j)]:
                return dp[(i,j)]
            dp[(i,j)] = 1
            for nx, ny in d:
                p,q = i+nx, j+ny
                if 0<=p<m and 0<=q<n:
                    if mat[p][q] > mat[i][j]:
                        dp[(i,j)] = max(dp[(i,j)], 1+dfs(p,q))
            return dp[(i,j)]

        d = [(1,0), (-1,0), (0,1), (0, -1)]
        dp = Counter()
        m,n = len(mat), len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
        return ans
