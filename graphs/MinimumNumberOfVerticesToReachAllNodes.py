import collections
from typing import List


# O(n + e) time || O(n + e) space
def find_smallest_set_of_vertices(self, n: int, edges: List[List[int]]) -> List[int]:
    def dfs(g, c, vis, res):
        vis[c] = True
        for adj in g[c]:
            if not vis[adj]:
                dfs(g, adj, vis, res)
            elif adj in res:
                res.remove(adj)

    g = collections.defaultdict(list)
    for e in edges:
        u, v = e
        g[u].append(v)

    res = set()
    vis = [False] * n
    for i in range(n):
        if not vis[i]:
            dfs(g, i, vis, res)
            res.add(i)

    return list(res)
