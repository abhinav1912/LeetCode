from collections import Counter
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if grid[i][j]:
                dp[(i,j)] = 0
                return 0
            if (i==m-1) and (j==n-1):
                return 1
            if dp[(i,j)]:
                return dp[(i,j)]
            x = dfs(i+1,j)+dfs(i,j+1)
            dp[(i,j)] = x
            return x
        dp = Counter()
        m,n = len(grid), len(grid[0])
        return dfs(0,0)
