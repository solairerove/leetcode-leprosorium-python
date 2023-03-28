import collections
from typing import List


# O(E * a(n)) time || O(V) space
# E - number of edges
# V - number of vertices
# a(n) - inverse Ackerman function

# O(n + e) time || O(n + e) space
def count_components_dfs(self, n: int, edges: List[List[int]]) -> int:
    adj = {x: [] for x in range(n)}
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    res = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res += 1
            dfs(self, i, adj, visit)

    return res


def dfs(self, node, adj, visit):
    visit[node] = True
    for neighbor in adj[node]:
        if not visit[neighbor]:
            dfs(self, neighbor, adj, visit)


# O(n + e) time || O(n + e) space
def count_components_bfs(self, n: int, edges: List[List[int]]) -> int:
    adj = {x: [] for x in range(n)}
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    res = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res += 1
            bfs(self, i, adj, visit)

    return res


def bfs(self, node, adj, visit):
    dq = collections.deque([node])
    visit[node] = True
    while dq:
        node = dq.popleft()
        for neighbor in adj[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                dq.append(neighbor)
