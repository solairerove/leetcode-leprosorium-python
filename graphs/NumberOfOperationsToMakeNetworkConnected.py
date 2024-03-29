import collections
from typing import List


# O(n + e) time || O(n + e) space
def make_connected_dfs(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    adj = {x: [] for x in range(n)}
    for x, y in connections:
        adj[x].append(y)
        adj[y].append(x)

    res = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res += 1
            dfs(self, i, adj, visit)

    return res - 1


def dfs(self, node, adj, visit):
    visit[node] = True
    for neighbor in adj[node]:
        if not visit[neighbor]:
            dfs(self, neighbor, adj, visit)


# O(n + e) time || O(n) space
def make_connected_bfs(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    adj = {x: [] for x in range(n)}
    for x, y in connections:
        adj[x].append(y)
        adj[y].append(x)

    res = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res += 1
            bfs(self, i, adj, visit)

    return res - 1


def bfs(self, node, adj, visit):
    dq = collections.deque([node])
    visit[node] = True
    while dq:
        node = dq.popleft()
        for neighbor in adj[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                dq.append(neighbor)


# O(n + e) time || O(n) space
def make_connected_union(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    dsu = UnionFind(n)
    number_of_connected_components = n
    for connection in connections:
        if dsu.find(connection[0]) != dsu.find(connection[1]):
            number_of_connected_components -= 1
            dsu.union_set(connection[0], connection[1])

    return number_of_connected_components - 1


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union_set(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)

        if self.rank[x_set] < self.rank[y_set]:
            self.parent[x_set] = y_set
        elif self.rank[x_set] > self.rank[y_set]:
            self.parent[y_set] = x_set
        else:
            self.parent[y_set] = x_set
            self.rank[x_set] += 1
