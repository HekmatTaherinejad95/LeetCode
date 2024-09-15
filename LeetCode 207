from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            g[b].append(a)
            in_degree[a] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for nei in g[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return visited == numCourses
