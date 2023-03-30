from typing import List


# O(n + e) time || O(n + e) space
def count_pairs(self, n: int, edges: List[List[int]]) -> int:
    adj = {x: [] for x in range(n)}
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    visit = [False] * n

    return sum((size := dfs(self, i, adj, visit)) * (n - size) for i in range(n) if not visit[i]) // 2


def dfs(self, node, adj, visit):
    if visit[node]:
        return 0

    visit[node] = True

    return sum(dfs(self, neighbor, adj, visit) for neighbor in adj[node]) + 1
