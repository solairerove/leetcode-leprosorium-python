import collections
from typing import List


# O(n + e) time || O(n) space
def min_reorder_bfs(self, n: int, connections: List[List[int]]) -> int:
    adj = {x: [] for x in range(n)}
    for x, y in connections:
        adj[x].append((y, 1))
        adj[y].append((x, 0))

    res = [0]
    visit = [False] * n
    bfs(self, 0, adj, visit, res)

    return res[0]


def bfs(self, node, adj, visit, res):
    dq = collections.deque([node])
    visit[node] = True
    while dq:
        node = dq.popleft()
        for neighbor, cost in adj[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                res[0] += cost
                dq.append(neighbor)


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
