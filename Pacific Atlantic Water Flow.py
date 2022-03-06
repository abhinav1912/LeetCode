class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.matrix = heights
        self.directions = [(1,0), (-1,0),(0,1),(0,-1)]
        m,n = len(heights), len(heights[0])
        pacific, atlantic = [[0 for i in range(n)] for i in range(m)], [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            self.dfs(i, 0, m, n, pacific)
            self.dfs(i, n-1, m, n, atlantic)
        for j in range(n):
            self.dfs(0, j, m, n, pacific)
            self.dfs(m-1, j, m, n, atlantic)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        return ans
    
    def dfs(self, i, j, m, n, visited):
        if visited[i][j]:
            return
        visited[i][j] = True
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if (0 <= x < m) and (0 <= y < n) and self.matrix[i][j] <= self.matrix[x][y]:
                self.dfs(x, y, m, n, visited)
