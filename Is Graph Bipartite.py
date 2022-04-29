from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0]*n
        for k in range(n):
            if not color[k]:
                color[k] = 1
                q = deque()
                q.append(k)
                while q:
                    x = q.popleft()
                    for i in graph[x]:
                        if not color[i]:
                            color[i] = 3 - color[x]
                            q.append(i)
                        elif color[i] == color[x]:
                            return False
        return True
