import collections
from typing import List


# O(n + e) time || O(n + e) space
def min_reorder_dfs(self, n: int, connections: List[List[int]]) -> int:
    graph = collections.defaultdict(list)

    # don't like this
    # adj[connection[0]].append(connection[1]) is better for me
    # need to create some code practice
    for x, y in connections:
        graph[x].append((y, 1))
        graph[y].append((x, 0))

    # don't like this
    # like using [False] * n
    visited = {0}
    res = [0]
    dfs(self, 0, graph, visited, res)

    return res[0]


# don't like city, node is better
def dfs(self, city, graph, visited, res):
    visited.add(city)
    for neighbor, cost in graph[city]:
        if neighbor not in visited:
            visited.add(neighbor)
            res[0] += cost
            dfs(self, neighbor, graph, visited, res)
