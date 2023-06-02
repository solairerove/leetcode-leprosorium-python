import collections
from typing import List


# O(n^3) time || O(n^2) space
def maximum_detonation(self, bombs: List[List[int]]) -> int:
    n, res, adj = len(bombs), 0, collections.defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                adj[i] += [j]

    for i in range(n):
        visit = {i}
        dfs(self, i, adj, visit)
        res = max(res, len(visit))

    return res


def dfs(self, node, adj, visit):
    visit.add(node)
    for neighbor in adj[node]:
        if neighbor not in visit:
            dfs(self, neighbor, adj, visit)
