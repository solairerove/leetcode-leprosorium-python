import collections
from typing import List


# O(n + e) time || O(n + e) space
def make_connected_dfs(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    def dfs(node):
        visit[node] = True
        for neighbor in graph[node]:
            if not visit[neighbor]:
                dfs(neighbor)

    graph = [[] for _ in range(n)]
    for connection in connections:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])

    res = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res += 1
            dfs(i)

    return res - 1


# O(n + e) time || O(n) space
def make_connected_bfs(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    def bfs(node):
        dq = collections.deque([node])
        visit[node] = True
        while dq:
            node = dq.popleft()
            for neighbor in graph[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dq.append(neighbor)

    graph = [[] for _ in range(n)]
    for connection in connections:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])

    res = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            res += 1
            bfs(i)

    return res - 1


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
