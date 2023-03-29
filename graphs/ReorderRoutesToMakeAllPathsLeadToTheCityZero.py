import collections
from typing import List


# O(n + e) time || O(n) space
def min_reorder_bfs(self, n: int, connections: List[List[int]]) -> int:
    graph = collections.defaultdict(list)

    for u, v in connections:
        graph[u].append((v, 1))
        graph[v].append((u, 0))

    dq = collections.deque([0])
    visited = {0}
    res = 0
    while dq:
        city = dq.popleft()
        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                res += cost
                dq.append(neighbor)

    return res


# O(n + e) time || O(n + e) space
def min_reorder_dfs(self, n: int, connections: List[List[int]]) -> int:
    adj = {x: [] for x in range(n)}
    for x, y in connections:
        adj[x].append((y, 1))
        adj[y].append((x, 0))

    res = [0]
    visit = [False] * n
    dfs(self, 0, adj, visit, res)

    return res[0]


def dfs(self, node, adj, visit, res):
    visit[node] = True
    for neighbor, cost in adj[node]:
        if not visit[neighbor]:
            res[0] += cost
            dfs(self, neighbor, adj, visit, res)
