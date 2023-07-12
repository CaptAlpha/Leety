class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        safe = {}
        n = len(graph)

        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False

            for neighbour in graph[i]:
                if dfs(neighbour) is False:
                    return False
            safe[i] = True
            return safe[i]
        ans = []
        for i in range(n):
            if dfs(i): ans.append(i)
        return ans
