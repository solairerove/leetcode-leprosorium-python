import collections
from typing import List


# O(n + e) time || O(n) space
def shortest_alternating_paths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
    adj = {x: [] for x in range(n)}
    # use map here?
    for x, y in red_edges:
        adj[x].append((y, 0))

    for x, y in blue_edges:
        adj[x].append((y, 1))

    res = [-1] * n
    res[0] = 0

    visit = [[False, False] for _ in range(n)]
    visit[0][0] = visit[0][1] = True

    dq = collections.deque()
    dq.append((0, 0, 0))
    dq.append((0, 0, 1))

    while dq:
        node, steps, last_color = dq.popleft()
        for neighbor, color in adj[node]:
            if color != last_color and not visit[neighbor][color]:
                if res[neighbor] == -1:
                    res[neighbor] = steps + 1
                visit[neighbor][color] = True
                dq.append((neighbor, steps + 1, color))

    return res
