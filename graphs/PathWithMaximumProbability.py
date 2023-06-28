import collections
from typing import List


# O(n * e) time || O(n + e) space
def max_probability_bellman_ford(self, n: int, edges: List[List[int]], succ_prob: List[float], start: int, end: int) -> float:
    g, dq = collections.defaultdict(list), collections.deque([start])
    for i, (a, b) in enumerate(edges):
        g[a].append([b, i])
        g[b].append([a, i])

    p = [0.0] * n
    p[start] = 1.0
    while dq:
        curr = dq.popleft()
        for neighbor, i in g.get(curr, []):
            if p[curr] * succ_prob[i] > p[neighbor]:
                p[neighbor] = p[curr] * succ_prob[i]
                dq.append(neighbor)

    return p[end]
