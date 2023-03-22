import sys
from typing import List


class Solution:
    def __init__(self):
        self.answer = sys.maxsize

    def dfs(self, node, adj, visit):
        visit[node] = True

        if node not in adj:
            return

        for edge in adj[node]:
            self.answer = min(self.answer, edge[1])
            if not visit[edge[0]]:
                self.dfs(edge[0], adj, visit)

    # O(n + e) time || O(n + e) space
    # n - number of nodes
    # e - number of edges
    def min_score(self, n: int, roads: List[List[int]]) -> int:
        adj = {}
        for road in roads:
            adj.setdefault(road[0], []).append([road[1], road[2]])
            adj.setdefault(road[1], []).append([road[0], road[2]])

        visit = [False] * (n + 1)
        self.dfs(1, adj, visit)

        return self.answer
