from typing import List


# O(n) time || O(n) space
def longest_cycle(self, edges: List[int]) -> int:
    n = len(edges)
    visit = set()
    ranks = [float('inf')] * n

    def dfs(node, rank):
        if node in visit or edges[node] == -1:
            return -1

        if ranks[node] < rank:
            return rank - ranks[node]

        ranks[node] = rank
        val = dfs(edges[node], rank + 1)
        visit.add(node)

        return val

    res = -1
    for node in range(n):
        cycle_len = dfs(node, 0)
        if cycle_len > 0:
            res = max(res, cycle_len)

    return res
