from typing import List


# O(n) time || O(n) space
def longest_cycle_dfs(self, edges: List[int]) -> int:
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


# O(n) time || O(n) space
def longest_cycle_kahn(self, edges: List[int]) -> int:
    n = len(edges)
    visit = [False] * n
    indegree = [0] * n

    for edge in edges:
        if edge != -1:
            indegree[edge] = indegree[edge] + 1

    q = []
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.pop(0)
        visit[node] = True
        neighbor = edges[node]

        if neighbor != -1:
            indegree[neighbor] = indegree[neighbor] - 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    res = -1
    for i in range(n):
        if not visit[i]:
            neighbor = edges[i]
            cnt = 1
            visit[i] = True
            while neighbor != i:
                visit[neighbor] = True
                cnt += 1
                neighbor = edges[neighbor]

            res = max(cnt, res)

    return res
