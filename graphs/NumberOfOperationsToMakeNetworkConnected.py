from typing import List


# O(n + e) time || O(n + e) space
def make_connected_dfs(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    adj = [[] for _ in range(n)]
    for connection in connections:
        adj[connection[0]].append(connection[1])
        adj[connection[1]].append(connection[0])

    number_of_connected_components = 0
    visit = [False for _ in range(n)]
    for i in range(n):
        if not visit[i]:
            number_of_connected_components += 1
            dfs(self, i, adj, visit)

    return number_of_connected_components - 1


def dfs(self, node, adj, visit):
    visit[node] = True
    for neighbor in adj[node]:
        if not visit[neighbor]:
            dfs(self, neighbor, adj, visit)
