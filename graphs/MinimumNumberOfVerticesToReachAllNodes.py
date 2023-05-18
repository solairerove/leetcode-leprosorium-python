import collections
from typing import List


# O(n + e) time || O(n + e) space
def find_smallest_set_of_vertices_dfs(self, n: int, edges: List[List[int]]) -> List[int]:
    adj = {x: [] for x in range(n)}
    for x, y in edges:
        adj[x].append(y)

    res = set()
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res.add(i)
            dfs(self, i, adj, visit, res)

    return list(res)


def dfs(self, node, adj, visit, res):
    visit[node] = True
    for neighbor in adj[node]:
        if not visit[neighbor]:
            dfs(self, neighbor, adj, visit, res)
        elif neighbor in res:
            res.remove(neighbor)


# O(n + e) time || O(n + e) space
def find_smallest_set_of_vertices_bfs(self, n: int, edges: List[List[int]]) -> List[int]:
    adj = {x: [] for x in range(n)}
    for x, y in edges:
        adj[x].append(y)

    res = set()
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res.add(i)
            bfs(self, i, adj, visit, res)

    return list(res)


def bfs(self, node, adj, visit, res):
    dq = collections.deque([node])
    visit[node] = True
    while dq:
        node = dq.popleft()
        for neighbor in adj[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                dq.append(neighbor)
            elif neighbor in res:
                res.remove(neighbor)
