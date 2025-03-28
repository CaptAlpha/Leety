class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def bfs(k):
            p = 0

            # Process until the min-heap is empty or the smallest element is >= k.
            while pq:
                if pq[0][0] >= k: break

                # Pop the cell with the smallest value & increase point.
                _, i, j = heappop(pq)
                p += 1

                for d in directions:
                    i_, j_ = i + d[0], j + d[1]
                    if 0 <= i_ < n and 0 <= j_ < m and grid[i_][j_] > 0:
                        heappush(pq, (grid[i_][j_], i_, j_))
                        # Mark the cell as visited by setting it to -1.
                        grid[i_][j_] = -1
            
            return p
        
        points = defaultdict(int)  # Maps k -> point
        point = 0  # Accumulated points so far.
        
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Initialize min-heap with the starting cell (top-left corner).
        pq = [(grid[0][0], 0, 0)]
        # Mark the starting cell as visited.
        grid[0][0] = -1

        # Process each unique query in ascending order.
        for k in sorted(set(queries)):
            point += bfs(k)
            points[k] = point  # Save the cumulative points for query k.

        # Return the results for the original order of queries.
        return [points[k] for k in queries]