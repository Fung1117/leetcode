from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph using adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        
        def dfs(node):
            visited[node] = True
            nodes = [node]
            for next_node in graph[node]:
                if not visited[next_node]:
                    nodes.extend(dfs(next_node))
            return nodes

        def is_complete_component(component):
            size = len(component)
            # A complete component should have size * (size - 1) / 2 edges
            edge_count = sum(len(graph[node]) for node in component) // 2
            return edge_count == (size * (size - 1)) // 2

        complete_count = 0
        for i in range(n):
            if not visited[i]:
                component = dfs(i)
                if is_complete_component(component):
                    complete_count += 1
        
        return complete_count