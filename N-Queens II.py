class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [0]
        self.dfs(n, 0, [-1]*n, res)
        return res[0]
    
    def dfs(self, n, index, path, res):
        if index == len(path):
            res[0] += 1
            return
        for i in range(n):
            path[index] = i
            if self.valid(index, path):
                self.dfs(n, index+1, path, res)
    
    def valid(self, n, path):
        for i in range(n+1):
            for j in range(i+1, n+1):
                if path[i] == -1 or path[j] == -1:
                    continue
                if (path[i] == path[j]) and path[i]!=-1:
                    return False
                if abs(path[i]-path[j]) == abs(i-j):
                    return False
        return True
