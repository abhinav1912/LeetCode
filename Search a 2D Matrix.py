class Solution:
    def searchMatrix(self, mat: List[List[int]], x: int) -> bool:
        i,j,m,n = 0,0, len(mat), len(mat[0])
        while i< m and j < n:
            if mat[i][-1] < x:
                i += 1
            elif mat[i][0] > x:
                return False
            elif mat[i][j] == x:
                return True
            elif mat[i][j] < x:
                j += 1
            else:
                return False
        return False
