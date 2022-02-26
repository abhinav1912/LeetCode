class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = {}
        def dfs(a,b):
            if a==m and b==n:
                return 1
            if a==m or b==n:
                return 1
            if map.get((a,b)):
                return map[(a,b)]
            map[(a,b)] = dfs(a+1,b) + dfs(a,b+1)
            return map[(a,b)]
        return dfs(1,1)
