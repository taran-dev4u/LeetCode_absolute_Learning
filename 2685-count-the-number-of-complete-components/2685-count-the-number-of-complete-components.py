from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True

            vertex_count = 0
            degree_sum = 0

            while stack:
                node = stack.pop()
                vertex_count += 1
                degree_sum += len(graph[node])

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            # A complete graph with k vertices has degree sum k * (k - 1).
            if degree_sum == vertex_count * (vertex_count - 1):
                complete_components += 1

        return complete_components