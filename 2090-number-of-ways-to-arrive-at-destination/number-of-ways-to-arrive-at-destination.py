import heapq
from typing import List

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def display(self):
        for i in range(self.n):
            print(f"{i}: {self.adj[i]}")

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Build the graph
        g = Graph(n)
        for u, v, w in roads:
            g.add_edge(u, v, w)
        
        # Dijkstra's Algorithm
        def dijkstra(graph, start):
            # Initialize distances and ways
            distances = [float('inf')] * n
            ways = [0] * n
            distances[start] = 0
            ways[start] = 1
            
            # Min-heap: (distance, node)
            pq = [(0, start)]
            
            while pq:
                current_distance, u = heapq.heappop(pq)
                
                # If the current distance is greater than the recorded distance, skip
                if current_distance > distances[u]:
                    continue
                
                # Explore neighbors
                for v, w in graph[u]:
                    distance = current_distance + w
                    
                    # If a shorter path is found
                    if distance < distances[v]:
                        distances[v] = distance
                        ways[v] = ways[u]  # Reset the number of ways
                        heapq.heappush(pq, (distance, v))
                    # If a path with the same distance is found
                    elif distance == distances[v]:
                        ways[v] = (ways[v] + ways[u]) % (10**9 + 7)
            
            # Return the number of ways to reach the destination
            return ways[n-1]
        
        # Call Dijkstra's algorithm starting from node 0
        return dijkstra(g.adj, 0)