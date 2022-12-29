from heapq import heapify, heappush, heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        t = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        t.sort()
        h, i = [(t[0][1], t[0][2])], 1
        ans = []
        heapify(h)
        time = t[0][0]
        while h:
            x = heappop(h)
            time += x[0]
            ans.append(x[1])
            while (i < n) and t[i][0] <= time:
                heappush(h, (t[i][1], t[i][2]))
                i += 1
            if (i < n) and (not h):
                time = t[i][0]
                heappush(h, (t[i][1], t[i][2]))
                i += 1
        return ans
