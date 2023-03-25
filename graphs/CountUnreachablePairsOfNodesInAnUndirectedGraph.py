import collections
from typing import List


# O(n + e) time || O(n + e) space
def count_pairs(self, n: int, edges: List[List[int]]) -> int:
    def dfs(node):
        if node in visited:
            return 0
        visited.add(node)

        return sum(dfs(nei) for nei in adj_list[node]) + 1

    adj_list = collections.defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()

    return sum((size := dfs(i)) * (n - size) for i in range(n) if i not in visited) // 2
