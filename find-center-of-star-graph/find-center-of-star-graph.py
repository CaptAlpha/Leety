class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = {}

        for i in edges:
            u, v = i[0], i[1]

            if u not in graph:
                graph[u] = []
            
            if v not in graph:
                graph[v] = []

        for i in edges:
            u, v = i[0], i[1]
            graph[u].append(v)
            graph[v].append(u)

        print(graph)
        star = -1
        m = 0

        for i, j in graph.items():
            m = max(len(j), m)
            if m == len(j):
                star = i
        return star
            
            