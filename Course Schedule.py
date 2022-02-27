class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in prerequisites:
            graph.setdefault(i[1], []).append(i[0])
        visit = [0]*numCourses
        def cycle(i):
            if visit[i]==1:
                return False
            if visit[i]==-1:
                return True
            visit[i] = -1
            for neighbour in graph.get(i, []):
                if cycle(neighbour):
                    return True
            visit[i] = 1
            return False
        for i in range(numCourses):
            if cycle(i):
                return False
        return True
