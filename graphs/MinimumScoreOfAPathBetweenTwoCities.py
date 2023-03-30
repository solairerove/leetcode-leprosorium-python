from typing import List


# O(n + e) time || O(n + e) space
# n - number of nodes
# e - number of edges
def min_score(self, n: int, roads: List[List[int]]) -> int:
    adj = {x: [] for x in range(1, n + 1)}
    for x, y, z in roads:
        adj[x].append((y, z))
        adj[y].append((x, z))

    res = [float('inf')]
    visit = [False] * (n + 1)
    dfs(self, 1, adj, visit, res)

    return int(res[0])


def dfs(self, node, adj, visit, res):
    visit[node] = True
    for neighbor, score in adj[node]:
        res[0] = min(res[0], score)
        if not visit[neighbor]:
            dfs(self, neighbor, adj, visit, res)
