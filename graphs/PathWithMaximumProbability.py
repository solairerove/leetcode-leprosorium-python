import collections
import heapq
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


# O((n + e) * log(e)) time || O(n + e) space
def max_probability_dijkstra(self, n: int, edges: List[List[int]], succ_prob: List[float], start: int,
                             end: int) -> float:
    p, g = [0.0] * n, collections.defaultdict(list)
    for index, (a, b) in enumerate(edges):
        g[a].append((b, index))
        g[b].append((a, index))

    p[start] = 1.0
    heap = [(-p[start], start)]
    while heap:
        prob, curr = heapq.heappop(heap)
        if curr == end:
            return -prob

        for neighbor, index in g.get(curr, []):
            if -prob * succ_prob[index] > p[neighbor]:
                p[neighbor] = -prob * succ_prob[index]
                heapq.heappush(heap, (-p[neighbor], neighbor))

    return 0.0
