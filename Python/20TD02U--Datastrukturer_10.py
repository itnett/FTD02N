python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        result = []
        self._dfs_util(start, visited, result)
        return result

    def _dfs_util(self, v, visited, result):
        visited.add(v)
        result.append(v)
        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self._dfs_util(neighbour, visited, result)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []
        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                result.append(v)
                queue.extend([neighbour for neighbour in self.graph.get(v, []) if neighbour not in visited])
        return result

    def display(self):
        return self.graph