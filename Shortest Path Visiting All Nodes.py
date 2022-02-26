from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodes = len(graph)
        steps = 0
        masks = [1<<i for i in range(nodes)]
        visited_masks = [{masks[i]} for i in range(nodes)]
        all_visited = (1<<nodes)-1
        queue = deque([(i, 1<<i) for i in range(nodes)])
        while queue:
            count = len(queue)
            while count:
                curr, visited = queue.popleft()
                if visited == all_visited:
                    return steps
                for neighbor in graph[curr]:
                    new_visited = visited | masks[neighbor]
                    if new_visited == all_visited:
                        return steps+1
                    if new_visited not in visited_masks[neighbor]:
                        visited_masks[neighbor].add(new_visited)
                        queue.append((neighbor, new_visited))
                count -= 1
            steps += 1
        return -1
