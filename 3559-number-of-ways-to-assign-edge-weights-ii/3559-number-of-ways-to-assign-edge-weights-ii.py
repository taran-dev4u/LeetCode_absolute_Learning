from collections import deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        max_log = n.bit_length()
        up = [[0] * (n + 1) for _ in range(max_log)]
        depth = [0] * (n + 1)

        queue = deque([1])
        seen = [False] * (n + 1)
        seen[1] = True

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if seen[neighbor]:
                    continue
                seen[neighbor] = True
                depth[neighbor] = depth[node] + 1
                up[0][neighbor] = node
                queue.append(neighbor)

        for bit in range(1, max_log):
            prev = up[bit - 1]
            curr = up[bit]
            for node in range(1, n + 1):
                curr[node] = prev[prev[node]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            gap = depth[a] - depth[b]
            bit = 0
            while gap:
                if gap & 1:
                    a = up[bit][a]
                gap >>= 1
                bit += 1

            if a == b:
                return a

            for bit in range(max_log - 1, -1, -1):
                if up[bit][a] != up[bit][b]:
                    a = up[bit][a]
                    b = up[bit][b]

            return up[0][a]

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % mod

        answer = []
        for u, v in queries:
            ancestor = lca(u, v)
            distance = depth[u] + depth[v] - 2 * depth[ancestor]
            answer.append(0 if distance == 0 else pow2[distance - 1])

        return answer