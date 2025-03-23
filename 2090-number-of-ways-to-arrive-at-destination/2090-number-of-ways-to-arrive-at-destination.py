class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Build the graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra's algorithm initialization
        min_time = [float('inf')] * n
        min_time[0] = 0
        path_count = [0] * n
        path_count[0] = 1
        
        # Priority queue for Dijkstra's algorithm
        priority_queue = [(0, 0)]  # (time, node)
        
        while priority_queue:
            time, node = heapq.heappop(priority_queue)
            
            # If we pop a node with a longer time, we skip it
            if time > min_time[node]:
                continue
            
            # Explore neighbors
            for next_node, travel_time in graph[node]:
                new_time = time + travel_time
                
                # Found a new shorter path to next_node
                if new_time < min_time[next_node]:
                    min_time[next_node] = new_time
                    path_count[next_node] = path_count[node]
                    heapq.heappush(priority_queue, (new_time, next_node))
                # Found another shortest path to next_node
                elif new_time == min_time[next_node]:
                    path_count[next_node] = (path_count[next_node] + path_count[node]) % MOD
        
        return path_count[n - 1]