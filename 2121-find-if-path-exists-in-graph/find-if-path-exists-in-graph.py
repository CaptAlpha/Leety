from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        flag = False
        
        def dfs(node):
            nonlocal flag
            if node in visited:
                return
            
            visited.add(node)
            if node == destination:
                flag = True
                return
            
            for neighbours in graph[node]:
                dfs(neighbours)
        
        dfs(source)
        return flag