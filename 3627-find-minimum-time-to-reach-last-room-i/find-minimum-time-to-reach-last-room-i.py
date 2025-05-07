import heapq

class Solution:

    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (time, row, col)

        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while pq:
            time, row, col = heapq.heappop(pq)
            if row == n - 1 and col == m - 1:
                return time

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m:
                    new_time = max(time + 1, moveTime[nr][nc] + 1 if time < moveTime[nr][nc] else time + 1)
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(pq, (new_time, nr, nc))

        return dist[n - 1][m - 1]