from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        heap = [(0,0,0)]
        n, m = len(heights), len(heights[0])
        visited = set()
        ans = 0
        while heap:
            d, x, y = heappop(heap)
            ans = max(ans, d)
            if (x, y) == (n-1, m-1):
                return ans
            visited.add((x,y))
            for nx, ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if (0 <= nx < n) and (0 <= ny < m) and (nx,ny) not in visited:
                    d = abs(heights[x][y]-heights[nx][ny])
                    heappush(heap,(d,nx,ny))
        return ans
