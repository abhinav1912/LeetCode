class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(curr, path):
            if curr == (n-1):
                return [path + [n-1]]
            ans = []
            for i in graph[curr]:
                ans.extend(dfs(i, path + [curr]))
            return ans
        n = len(graph)
        return dfs(0, [])
