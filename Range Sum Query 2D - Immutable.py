class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        m,n = len(mat), len(mat[0])
        self.s = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            self.s[i][0] = mat[i][0]
            for j in range(1, n):
                self.s[i][j] += self.s[i][j-1] + mat[i][j]
        for i in range(1, m):
            for j in range(n):
                self.s[i][j] += self.s[i-1][j]
        for i in self.s:
            print(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x = self.s[row2][col2]
        if col1:
            x -= self.s[row2][col1-1]
        if row1:
            x -= self.s[row1-1][col2]
            if col1:
                x += self.s[row1-1][col1-1]
        return x

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
