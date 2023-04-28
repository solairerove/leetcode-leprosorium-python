import collections
from typing import List


# O(n^2 * m) time || O(n + e) space
def num_similar_groups_bfs(self, strs: List[str]) -> int:
    adj = collections.defaultdict(list)
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if are_neighbors(self, strs[i], strs[j]):
                adj[strs[i]].append(strs[j])
                adj[strs[j]].append(strs[i])

    res = 0
    visit = set()
    for i in range(len(strs)):
        if strs[i] not in visit:
            res += 1
            bfs(self, strs[i], adj, visit)

    return res


def are_neighbors(self, a, b):
    dif = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dif += 1

    return dif == 0 or dif == 2


def bfs(self, node, adj, visit):
    dq = collections.deque([node])
    visit.add(node)
    while dq:
        node = dq.popleft()
        for neighbor in adj[node]:
            if neighbor not in visit:
                visit.add(neighbor)
                dq.append(neighbor)
