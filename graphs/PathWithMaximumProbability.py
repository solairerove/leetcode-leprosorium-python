import collections
from typing import List


# O(n * e) time || O(n + e) space
def max_probability_bellman_ford(self, n: int, edges: List[List[int]], succ_prob: List[float], start: int,
                                 end: int) -> float:
    adj = {x: [] for x in range(n)}
    for i, (x, y) in enumerate(edges):
        adj[x].append([y, i])
        adj[y].append([x, i])

    res = [0.0] * n
    res[start] = 1.0
    dq = collections.deque([start])
    while dq:
        node = dq.popleft()
        for neighbor, i in adj.get(node, []):
            if res[node] * succ_prob[i] > res[neighbor]:
                res[neighbor] = res[node] * succ_prob[i]
                dq.append(neighbor)

    return res[end]
