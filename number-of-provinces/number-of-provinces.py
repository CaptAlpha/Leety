class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            visited[city] = True
            for nextCity in range(n):
                if isConnected[city][nextCity] == 1 and not visited[nextCity]:
                    dfs(nextCity)

        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces