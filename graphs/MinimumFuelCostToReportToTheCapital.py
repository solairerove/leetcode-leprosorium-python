import collections
import math
from typing import List


# O(n + e) time || O(n + e) space
def minimum_fuel_cost_dfs(self, roads: List[List[int]], seats: int) -> int:
    n = len(roads) + 1
    adj = [[] for _ in range(n)]
    for road in roads:
        adj[road[0]].append(road[1])
        adj[road[1]].append(road[0])

    self.fuel = 0

    def dfs(node, parent, adj, seats):
        representatives = 1
        for child in adj[node]:
            if child != parent:
                representatives += dfs(child, node, adj, seats)

        if node != 0:
            self.fuel += math.ceil(representatives / seats)

        return representatives

    dfs(0, -1, adj, seats)

    return self.fuel


# O(n + e) time || O(n) space
def minimum_fuel_cost_bfs(self, roads: List[List[int]], seats: int) -> int:
    n = len(roads) + 1
    adj = [[] for _ in range(n)]
    degree = [0] * n

    for road in roads:
        adj[road[0]].append(road[1])
        adj[road[1]].append(road[0])
        degree[road[0]] += 1
        degree[road[1]] += 1

    return bfs(self, n, adj, degree, seats)


def bfs(self, n, adj, degree, seats):
    dq = collections.deque()
    for i in range(1, n):
        if degree[i] == 1:
            dq.append(i)

    representatives = [1] * n
    fuel = 0

    while dq:
        node = dq.popleft()
        fuel += math.ceil(representatives[node] / seats)
        for neighbor in adj[node]:
            degree[neighbor] -= 1
            representatives[neighbor] += representatives[node]
            if degree[neighbor] == 1 and neighbor != 0:
                dq.append(neighbor)

    return fuel
