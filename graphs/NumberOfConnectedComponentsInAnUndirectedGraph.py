from typing import List


# O(E * a(n)) time || O(V) space
# E - number of edges
# V - number of vertices
# a(n) - inverse Ackerman function

# O(n + e) time || O(n + e) space
def count_components_dfs(self, n: int, edges: List[List[int]]) -> int:
    visited = [0] * n
    g = {x: [] for x in range(n)}
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    res = 0
    for i in range(n):
        if not visited[i]:
            dfs(self, i, g, visited)
            res += 1

    return res


def dfs(self, n, g, visited):
    if visited[n]:
        return

    visited[n] = 1
    for x in g[n]:
        dfs(self, x, g, visited)
