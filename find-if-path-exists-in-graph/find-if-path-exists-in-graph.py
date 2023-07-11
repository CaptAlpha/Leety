class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}

        for i in edges:
            u, v = i[0], i[1]

            graph[u] = []
            graph[v] = []

        for i in edges:
            u, v = i[0], i[1]

            graph[u].append(v)
            graph[v].append(u)

        def dfs(graph, node, visited):
            print(node, destination)
            if node == destination:
                return True
            visited.add(node)
            for item in graph[node]:
                if item not in visited:
                    if dfs(graph, item, visited):
                        return True
            return False

        
        visited = set()
        return dfs(graph, source, visited)
        
