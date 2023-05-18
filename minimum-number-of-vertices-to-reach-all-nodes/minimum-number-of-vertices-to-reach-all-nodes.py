class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        visited = set()
        res = set()

        for i,j in edges:
            graph[i].add(j)
        
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
                elif child in res:
                    res.remove(child)

        for i in range(n):
            if i not in visited:
                res.add(i)
                dfs(i)
        return res
